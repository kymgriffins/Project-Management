from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register( Project)
admin.site.register(Material)
admin.site.register( Comment)
admin.site.register(MaterialUsage)
admin.site.register(Invoice)
admin.site.register(DailyRecord)
admin.site.register(Blueprint)
admin.site.register(InvoiceItem)
admin.site.register(RecordPics)