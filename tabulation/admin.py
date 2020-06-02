from django.contrib import admin

# Register your models here.


from .models import HatchRecord, HatchDetail
 
# Register your models here.
admin.site.register(HatchRecord)
admin.site.register(HatchDetail)
