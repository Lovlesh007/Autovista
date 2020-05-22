from django.contrib import admin
from .models import Leads
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin

admin.site.site_header = 'AutoVista DashBoard'
admin.site.index_title = 'AutoVista'

admin.site.site_title = 'AutoVista'

class change(ImportExportActionModelAdmin):
    list_display =('Name','Phone','Email_address','Interested_in')
    search_fields=('Name','Email_address')


admin.site.register(Leads,change)