from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Invoice, InvoiceItem, Todo

import decimal


@receiver(m2m_changed, sender=Invoice.invoices.through)
def update_invoice_total_amount(sender, instance,action, **kwargs):
    if action == 'post_add':
    
        amount = decimal.Decimal(0.00)

        for invoice_item in instance.invoices.all():
            amount += decimal.Decimal(invoice_item.quantity) * decimal.Decimal(invoice_item.amount)

        instance.amount = amount
        instance.save()
    # print(f"Signal triggered for Invoice ID: {invoice.id}")
    
@receiver(post_save, sender=Todo)
def update_is_complete(sender, instance, created, **kwargs):
    if not created:  # Only update if the instance already exists, not on creation
        if instance.notes:  # Check if notes field is not empty
            instance.isComplete = True
        else:
            instance.isComplete = False
        instance.save()