from django.contrib import admin

# Register your models here.
from .models import Doctor, Patient, PatientPrescriptionDetails
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class PatientPrescriptionDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(PatientPrescriptionDetails, PatientPrescriptionDetailsAdmin)