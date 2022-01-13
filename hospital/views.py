from django.shortcuts import render,redirect,reverse
#from . import forms,models

from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings

# Create your views here.
def home_view(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')





# #for showing signup/login button for doctor
# def doctorclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request,'hospital/doctorclick.html')



# def doctor_signup_view(request):
#     userForm=forms.DoctorUserForm()
#     doctorForm=forms.DoctorForm()
#     mydict={'userForm':userForm,'doctorForm':doctorForm}
#     if request.method=='POST':
#         userForm=forms.DoctorUserForm(request.POST)
#         doctorForm=forms.DoctorForm(request.POST,request.FILES)
#         if userForm.is_valid() and doctorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             doctor=doctorForm.save(commit=False)
#             doctor.user=user
#             doctor=doctor.save()
#             my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
#             my_doctor_group[0].user_set.add(user)
#         return HttpResponseRedirect('doctorlogin')
#     return render(request,'hospital/doctorsignup.html',context=mydict)

