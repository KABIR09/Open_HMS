from django.db import models
from django.contrib.auth.models import User

# Create your models here.

departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists',
                'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


criticality = [('low', 'low'), ('intermediate',
                                'intermediate'), ('high', 'high')]


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    allergy_substance = models.CharField(max_length=100)
    allergy_criticality = models.CharField(
        max_length=20, choices=criticality, default='low')
    problems_list = models.CharField(max_length=100, null=False)
    immunization = models.CharField(max_length=100, null=False)
    history_procedure = models.CharField(max_length=100, null=False)
    diagnostic_results = models.FileField(
        upload_to='patient_document/', null=True, blank=True)
    past_history_of_illness = models.CharField(max_length=100, null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"
