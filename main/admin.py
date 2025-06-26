from django.contrib import admin
from .models import Service, ServiceType

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'price')

class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'slug')

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
