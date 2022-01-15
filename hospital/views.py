from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages




# Create your views here.


def home_view(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/index.html')

def contactus_view(request):
    return render(request, 'hospital/contactus.html')

# for showing signup/login button for doctor
def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/doctorclick.html')


def doctor_signup_view(request):
    userForm = forms.DoctorUserForm()
    doctorForm = forms.DoctorForm()
    mydict = {'userForm': userForm, 'doctorForm': doctorForm}
    if request.method == 'POST':
        userForm = forms.DoctorUserForm(request.POST)
        doctorForm = forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save(commit=False)
            doctor.user = user
            doctor = doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        else:
            messages.error(request, "Doctor Already Exists!!")
            return redirect('doctorsignup')
        return HttpResponseRedirect('doctorlogin')
    return render(request, 'hospital/doctorsignup.html', context=mydict)


def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
# change1


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def afterlogin_view(request):

    if is_doctor(request.user):
        return redirect('doctor-dashboard')
    elif is_patient(request.user):
        return redirect('patient-dashboard')
    # return redirect('doctor-dashboard')

    # elif is_patient(request.user):
    #     accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
    #     if accountapproval:
    #         return redirect('patient-dashboard')
    #     else:
    #         return render(request,'hospital/patient_wait_for_approval.html')


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    # #for three cards
    # patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
    # appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    # patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    # #for  table in doctor dashboard
    # appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    # patientid=[]
    # for a in appointments:
    #     patientid.append(a.patientId)
    # patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    # appointments=zip(appointments,patients)
    # mydict={
    # 'patientcount':patientcount,
    # 'appointmentcount':appointmentcount,
    # 'patientdischarged':patientdischarged,
    # 'appointments':appointments,
    # 'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    # }
    # return render(request,'hospital/doctor_dashboard.html',context=mydict)
    mydict = {
        'doctor': models.Doctor.objects.get(user_id=request.user.id),

    }
    return render(request, 'hospital/doctor_dashboard.html', context=mydict)


def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'hospital/patientclick.html')


def patient_signup_view(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.assignedDoctorId = request.POST.get('assignedDoctorId')
            patient = patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        else:
            messages.error(request, "Patient Already Exists!!!")
            return redirect('patientsignup')
        return HttpResponseRedirect('patientlogin')
    return render(request, 'hospital/patientsignup.html', context=mydict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    # patient=models.Patient.objects.get(user_id=request.user.id)
    # doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    # mydict={
    # 'patient':patient,
    # 'doctorName':doctor.get_name,
    # 'doctorMobile':doctor.mobile,
    # 'doctorAddress':doctor.address,
    # 'symptoms':patient.symptoms,
    # 'doctorDepartment':doctor.department,
    # 'admitDate':patient.admitDate,
    # }
    mydict = {
        'patient': models.Patient.objects.get(user_id=request.user.id),
    }

    return render(request, 'hospital/patient_dashboard.html', context=mydict)


# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_patient_search_view(request):
#     return render(request,'hospital/doctor_patient_search.html')


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_search_view(request):
    mydict = {
        'patients': models.Patient.objects.all().filter(assignedDoctorId=request.user.id),
         'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }
    if request.method == 'POST':
        mydict = {
            'patients': models.Patient.objects.all().filter(assignedDoctorId=request.user.id,user_id = request.POST['patId']),
            'doctor': models.Doctor.objects.get(user_id=request.user.id),
        }
    return render(request, 'hospital/doctor_patient.html', context=mydict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def prescription_patient_view(request,pk):
    patient = models.Patient.objects.get(id=pk)
    # days=(date.today()-patient.admitDate) #2 days, 0:00:00
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    # d=days.days # only how many day that is 2
    pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
    
    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        # 'admitDate': patient.admitDate,
        # 'day':d,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD':pDD
    }
    return render(request, 'hospital/patient_generate_prescription.html', context=patientDict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def new_prescription_patient_view(request,pk):
    patient = models.Patient.objects.get(id=pk)
    # days=(date.today()-patient.admitDate) #2 days, 0:00:00
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    # d=days.days # only how many day that is 2
    pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        # 'admitDate': patient.admitDate,
        # 'day':d,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD':pDD,
        'todayDate':date.today(),
         'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }
    return render(request, 'hospital/patient_new_prescription.html', context=patientDict)

    

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_add_medicine_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    # days=(date.today()-patient.admitDate) #2 days, 0:00:00
    #assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    # d=days.days # only how many day that is 2
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD0 = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        # 'admitDate': patient.admitDate,
        # 'day':d,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD':pDD0,
         'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }

    if request.method == 'POST':
       
        feeDict = {
            
            'medicationItem' : request.POST['medicationItem'],
            'frequency' : request.POST['frequency'],
            'dose' : request.POST['dose'],
            'doseUnit' : request.POST['doseUnit'],
            'directionDuration' : request.POST['directionDuration'],
            'form' : request.POST['form'],
            'additionalInstruc' : request.POST['additionalInstruc'],
            'substance' : request.POST['substance'],
            'date':date.today(),
            'todayDate':date.today()


        }
        
        patientDict.update(feeDict)
        # for updating to database patientDischargeDetails (pDD)
        pDD = models.PatientPrescriptionDetails()
        pDD.patientId = pk
        # pDD.patientName=patient.get_name
        # pDD.assignedDoctorName=assignedDoctor[0].first_name
        # pDD.address=patient.address
        # pDD.mobile=patient.mobile
        # pDD.symptoms=patient.symptoms
        # pDD.admitDate=patient.admitDate
        # pDD.releaseDate=date.today()
        # pDD.daySpent=int(d)
        pDD.date=date.today()
        pDD.medicationItem = request.POST['medicationItem']
        pDD.frequency = request.POST['frequency']
        pDD.dose = request.POST['dose']
        pDD.doseUnit = request.POST['doseUnit']
        pDD.directionDuration = request.POST['directionDuration']
        pDD.form = request.POST['form']
        pDD.additionalInstruc = request.POST['additionalInstruc']
        pDD.substance = request.POST['substance']
        pDD.save()
        return render(request, 'hospital/patient_new_prescription.html', context=patientDict)
    return render(request, 'hospital/doctor_add_medicine.html', context=patientDict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_medicine_view(request,pk,mpk):
# def post_delete_view(request,id):
#     #post=Post.objects.filter(id=id)
#     post=Post.objects.filter(id=id).first()
#     if request.user==post.author:
#         if request.method=='POST':
#             post.delete()
#             return redirect('posts:list')
#         else:
#             return render(request,'posts/delete.html')
#     else:
#         return redirect('posts:list')
    delete_dict={
        'patientId':pk,
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }
    medicine = models.PatientPrescriptionDetails.objects.all().filter(pk=mpk)
    if request.method=='POST':
        medicine.delete()
        patient = models.Patient.objects.get(id=pk)
        # days=(date.today()-patient.admitDate) #2 days, 0:00:00
        assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
        # d=days.days # only how many day that is 2
        pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
        patientDict = {
            'patientId': pk,
            'name': patient.get_name,
            'mobile': patient.mobile,
            'address': patient.address,
            'symptoms': patient.symptoms,
            # 'admitDate': patient.admitDate,
            # 'day':d,
            'assignedDoctorName': assignedDoctor[0].first_name,
            'pDD':pDD,
            'todayDate':date.today(),
             'doctor': models.Doctor.objects.get(user_id=request.user.id),
        }
        return render(request, 'hospital/patient_new_prescription.html', context=patientDict)

    return render(request,'hospital/doctor_delete_medicine.html',context=delete_dict)
    
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def old_prescription_patient_view(request,pk):
    patient = models.Patient.objects.get(id=pk)
    # days=(date.today()-patient.admitDate) #2 days, 0:00:00
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    # d=days.days # only how many day that is 2
    pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk).order_by('-date')
    
    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        # 'admitDate': patient.admitDate,
        # 'day':d,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD':pDD
    }
    return render(request, 'hospital/patient_old_prescription.html', context=patientDict)



#edited this -for patient Group-G

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_prescription_view(request):
    patient = models.Patient.objects.get(user_id=request.user.id)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=patient.id).order_by('-date')
    
    patientDict = {
        'patientId': patient.user_id,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        # 'admitDate': patient.admitDate,
        # 'day':d,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD':pDD,
        'patient': models.Patient.objects.get(user_id=request.user.id),
    }
    return render(request, 'hospital/prescription_patient.html', context=patientDict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def summary_patient_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    patientDict = {
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'todayDate': date.today(),
        'assignedDoctorName': assignedDoctor[0].first_name,
        'allergy_substance': patient.allergy_substance,
        'allergy_criticality': patient.allergy_criticality,
        'problems_list': patient.problems_list,
        'immunization': patient.immunization,
        'history_procedure': patient.history_procedure,
        'past_history_of_illness': patient.past_history_of_illness,
        'diagnostic_results': patient.diagnostic_results
    }

    return render(request, 'hospital/patient_summary.html', context=patientDict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_summary_view(request):
    patient = models.Patient.objects.get(user_id=request.user.id)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    patientDict = {
        'patientId': patient.user_id,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        
        'todayDate': date.today(),
        'assignedDoctorName': assignedDoctor[0].first_name,
        'allergy_substance': patient.allergy_substance,
        'allergy_criticality': patient.allergy_criticality,
        'problems_list': patient.problems_list,
        'immunization': patient.immunization,
        'history_procedure': patient.history_procedure,
        'past_history_of_illness': patient.past_history_of_illness,
        'diagnostic_results': patient.diagnostic_results,
        'patient': models.Patient.objects.get(user_id=request.user.id),
    }

    return render(request, 'hospital/summary_patient.html', context=patientDict)