from django.contrib import admin

# Register your models here.
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)