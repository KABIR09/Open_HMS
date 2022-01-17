from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

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


criticality = [('None','None'),('Low', 'Low'), ('Intermediate','Intermediate'), ('High', 'High')]


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



class PatientPrescriptionDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    medicationItem=models.CharField(max_length=100)
    frequency=models.PositiveIntegerField(null=False)
    dose=models.FloatField(null=False)
    doseUnit=models.CharField(max_length=100)
    directionDuration=models.CharField(max_length=200)
    form=models.CharField(max_length=100)
    additionalInstruc=models.CharField(max_length=400)
    substance=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)

    safetyAmount=models.PositiveIntegerField(null=False)
    safetyDoseUnit=models.CharField(max_length=400)
    safetyAllowedPer=models.CharField(max_length=400)
  
    orderStatus=models.CharField(max_length=100)

    orderDateDisc=models.DateTimeField(blank=True,default=datetime.now)
    orderDateWritten=models.DateTimeField(blank=True,default=datetime.now)

    authRepeat=models.PositiveIntegerField(null=False,blank=True)
    authValPer=models.DateTimeField(blank=True,default=datetime.now)


    dispInstruc=models.CharField(max_length=100,blank=True)
    dispDescrip=models.CharField(max_length=100,blank=True)
    dispAmount=models.PositiveIntegerField(null=False,blank=True)
    dispAmountUnits=models.CharField(max_length=200,blank=True)
    dispDurution=models.CharField(max_length=200,blank=True)


   

    @property
    def get_id(self):
        return self.user.id