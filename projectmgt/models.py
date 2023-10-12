from django.db import models
from authentication.models import User
from cloudinary.models import CloudinaryField

from django.utils import timezone


class Project(models.Model):
    PHASE_CHOICES = [
        ('designing', 'Designing'),
        ('approvals', 'Approvals'),
        ('ground_breaking', 'Ground Breaking'),
        ('substructure', 'Substructure'),
        ('superstructure', 'Superstructure'),
        ('finishes', 'Finishes'),
        ('handing_over', 'Handing Over'),
    ]
    current_phase = models.CharField(max_length=255, choices=PHASE_CHOICES, default='designing')
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True, auto_now_add=True) 
    end_date = models.DateField(blank=True, null=True)
    blueprints = models.ManyToManyField('Blueprint', blank=True, related_name="blueprints")
    phases = models.CharField(max_length=255, choices=PHASE_CHOICES)
    current_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervised_projects')
    architect = models.ForeignKey(User, on_delete=models.CASCADE, related_name='architect_projects')
    foreman = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foreman_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    payments = models.ManyToManyField("Payment", blank=True, related_name='project_payments')
    

    def __str__(self):
        return self.name
       

    def get_next_phase(self):
        # Define a method to get the next phase based on the current phase
        current_phase_index = [choice[0] for choice in self.PHASE_CHOICES].index(self.current_phase)
        
        if current_phase_index < len(self.PHASE_CHOICES) - 1:
            return self.PHASE_CHOICES[current_phase_index + 1][0]
        else:
            return None

    def move_to_next_phase(self):
        # Define a method to move the project to the next phase
        next_phase = self.get_next_phase()
        if next_phase:
            self.current_phase = next_phase
            self.save()

    def is_last_phase(self):
        # Define a method to check if the project is in the last phase
        return self.current_phase == self.PHASE_CHOICES[-1][0]
   
class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
    ('received', 'Received'),
    ('pending', 'Pending'),
    ('overdue', 'Overdue'),]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES)
     
class Building(models.Model):
    floors = models.IntegerField()
    square_feet = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='buildings')

    def __str__(self):
        return self.name

class Blueprint(models.Model):
    image = CloudinaryField("Blueprints", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.blueprints.add(self)


class RecordPics(models.Model):
    image = CloudinaryField("Blueprints", null=True, blank=True)
    daily_record = models.ForeignKey('DailyRecord', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.daily_record:
            self.daily_record.documents.add(self)
class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit =  models.CharField(max_length=255)


class MaterialUsage(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    daily_record = models.ForeignKey('DailyRecord', on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.daily_record:
            self.daily_record.materials.add(self)
    

class DailyRecord(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    work_completed = models.TextField(max_length=500, blank=True), 
    work_planned = models.TextField(max_length=500, blank=True)
    issues = models.TextField(max_length=500, blank=True)
    workers_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_spendings = models.DecimalField(max_digits=10, decimal_places=2)
    materials = models.ManyToManyField('MaterialUsage',  blank=True,related_name="materials")
    documents = models.ManyToManyField('RecordPics', blank=True, related_name="records")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_achieved = models.BooleanField(default=False)

class Invoice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    invoices = models.ManyToManyField('InvoiceItem',related_name='invoices')
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
class InvoiceItem(models.Model):
    materials =models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.amount = sum(item.materials.unit_cost * item.quantity for item in self.invoices.all())
        self.save()
    
class Comment(models.Model):
    daily_record = models.ForeignKey(DailyRecord, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    