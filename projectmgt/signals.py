from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Invoice, InvoiceItem

import decimal


# @receiver(m2m_changed, sender=Invoice.invoices.through)
# def update_invoice_total_amount(sender, instance,action, **kwargs):
#     if action == 'post_add':
    
#         amount = decimal.Decimal(0.00)

#         for item in instance.items.all():
#             amount += decimal.Decimal(quantity) * decimal.Decimal(invoice_item.amount)

#         instance.amount = amount
#         instance.save()
#     # print(f"Signal triggered for Invoice ID: {invoice.id}")
#     print(f"Total Amount updated to: {amount}")
