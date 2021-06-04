from django.contrib import admin

from .models import Service,Master,Certificate

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','price','master']
admin.site.register(Service,ServiceAdmin)


class MasterAdmin(admin.ModelAdmin):
    list_display = ['full_name','photo','exp','birth_date']
admin.site.register(Master,MasterAdmin)

class CertAdmin(admin.ModelAdmin):
    list_display = ['name','date_graduate','date_expired','status']
admin.site.register(Certificate,CertAdmin)
