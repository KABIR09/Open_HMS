from django import forms
from django.contrib.auth.models import User
from . import models

# Doctor form


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address', 'mobile', 'department', 'profile_pic']
# Patient


class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
    # this is the extrafield for linking patient and their assigend doctor
    # this will show dropdown __str__ method doctor model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all(
    ), empty_label="Name and Department", to_field_name="user_id")

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'symptoms', 'profile_pic', 'allergy_substance', 'allergy_criticality',
                  'problems_list', 'immunization', 'history_procedure', 'diagnostic_results', 'past_history_of_illness']
