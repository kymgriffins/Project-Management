from django.db import models
from authentication.models import User
from cloudinary.models import CloudinaryField

from django.utils import timezone
from decimal import Decimal

class Project(models.Model):
    # Client Details 
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    # Site Visit of the project
    coordinates = models.CharField(max_length=255)
    topology = models.TextField(blank=True)
    flora_fauna = models.TextField(blank=True)
    accesibility = models.TextField(blank=True)
    site_boundaries = models.TextField(blank=True)
    
    utilities_availability = models.TextField(blank=True)
    zoning_regulations = models.TextField(blank=True)
    permits_approvals= models.TextField(blank=True)
    safety_security= models.TextField(blank=True)
    staging_storing = models.TextField(blank=True)
    cultural_influences = models.TextField(blank=True)
    local_contacts = models.TextField(blank=True)
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
    
    # Documents section 
    blueprints = models.ManyToManyField('Blueprint', blank=True, related_name="blueprints")
    renders = models.ManyToManyField('Renders', blank=True, related_name="renders")
    mep = models.ManyToManyField('MEP', blank=True, related_name="mep")
    architecturals = models.ManyToManyField('Architecturals', blank=True, related_name="architecturals")
    qs = models.ManyToManyField('QS', blank=True, related_name="qs")
    structurals =models.ManyToManyField('Structurals', blank=True, related_name="structurals")
    legals = models.ManyToManyField('Legals', blank=True, related_name="legals")
    

    def __str__(self):
        return self.name
       

   
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    invoices = models.ManyToManyField('InvoiceItem',related_name='invoices', blank=True)    
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
   
class InvoiceItem(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('material', 'Material'),
    )
    item_type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    content = models.TextField(blank=True)  # For text items
    materials =models.ForeignKey(Material, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Todo(models.Model):
    TAG_CHOICES = (
        ('team', 'Team'),
        ('low', 'Low'),
        ('high', 'High'),
        ('site', 'Site'),
    )
    title = models.CharField(max_length=300)
    assigned_to = models.ManyToManyField(User,blank=True,related_name="assigned")
    due_date = models.DateTimeField()
    tags = models.CharField(max_length=15)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects_task')
    created_at = models.DateTimeField(default=timezone.now)
    isComplete = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment,blank=True,related_name="comments") 
    budget = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    companyearnings = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    facilitation = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    labour = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes= models.TextField(null=True, blank=True)
    # documents = 
    def __str__(self):
        return self.title
    

class Renders(models.Model):
    images = CloudinaryField("Renders", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="render_images")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.renders.add(self)

class MEP(models.Model):
    images = CloudinaryField("MEP", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="mep_images")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.mep.add(self)

class Structurals(models.Model):
    images = CloudinaryField("Structurals", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="structural_images")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.structurals.add(self)

class QS(models.Model):
    images = CloudinaryField("QS", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="qs_images")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.qs.add(self)

class Architecturals(models.Model):
    images = CloudinaryField("Architecturals", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="architectural_images")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.architecturals.add(self)

class Legals(models.Model):
    images = CloudinaryField("Legals", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="legal_images")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.project:
            self.project.legals.add(self)
