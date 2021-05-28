from django.contrib import admin

from .models import Service,Master,Certificate


admin.site.register(Service)
admin.site.register(Master)
admin.site.register(Certificate)
