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
  
    assignedDoctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all(
    ), empty_label="Name and Department", to_field_name="user_id")

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'symptoms', 'profile_pic', 'allergy_substance', 'allergy_criticality',
                  'problems_list', 'immunization', 'history_procedure', 'diagnostic_results', 'past_history_of_illness']
