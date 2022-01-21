from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date
from django.conf import settings


from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.


def home_view(request):
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



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    mydict = {
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
        'patientcount':models.Patient.objects.all().filter(assignedDoctorId=request.user.id).count(),
         


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
    patient = models.Patient.objects.get(user_id=request.user.id)
    doctor = models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    mydict = {
        'patient': patient,
        'doctorName': doctor.get_name,
        'doctorMobile': doctor.mobile,
        'doctorAddress': doctor.address,
        'symptoms': patient.symptoms,
        'doctorDepartment': doctor.department,
    }

    return render(request, 'hospital/patient_dashboard.html', context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_search_view(request):
    mydict = {
        'patients': models.Patient.objects.all().filter(assignedDoctorId=request.user.id),
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }
    if request.method == 'POST':
        mydict = {
            'patients': models.Patient.objects.all().filter(assignedDoctorId=request.user.id, id=request.POST['patId']),
            'doctor': models.Doctor.objects.get(user_id=request.user.id),
        }
    return render(request, 'hospital/doctor_patient.html', context=mydict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def prescription_patient_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)

    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD': pDD
    }
    return render(request, 'hospital/patient_generate_prescription.html', context=patientDict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def new_prescription_patient_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD': pDD,
        'todayDate': date.today(),
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }
    return render(request, 'hospital/patient_new_prescription.html', context=patientDict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_add_medicine_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD0 = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD': pDD0,
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }

    if request.method == 'POST':

        feeDict = {

            'medicationItem': request.POST['medicationItem'],
            'frequency': request.POST['frequency'],
            'dose': request.POST['dose'],
            'doseUnit': request.POST['doseUnit'],
            'directionDuration': request.POST['directionDuration'],
            'form': request.POST['form'],
            'additionalInstruc': request.POST['additionalInstruc'],
            'substance': request.POST['substance'],
            'date': date.today(),
            'todayDate': date.today(),
            'safetyAmount': request.POST['safetyAmount'],
            'safetyDoseUnit': request.POST['safetyDoseUnit'],
            'safetyAllowedPer': request.POST['safetyAllowedPer'],
            'orderStatus': request.POST['orderStatus'],
            'orderDateDisc': request.POST['orderDateDisc'],
            'orderDateWritten': request.POST['orderDateWritten'],
            'authRepeat': request.POST['authRepeat'],
            'authValPer': request.POST['authValPer'],
            'dispInstruc': request.POST['dispInstruc'],
            'dispDescrip': request.POST['dispDescrip'],
            'dispAmount': request.POST['dispAmount'],
            'dispAmountUnits': request.POST['dispAmountUnits'],
            'dispDurution': request.POST['dispDurution'],
        }

        patientDict.update(feeDict)
        pDD = models.PatientPrescriptionDetails()
        pDD.patientId = pk
        pDD.date = date.today()
        pDD.medicationItem = request.POST['medicationItem']
        pDD.frequency = request.POST['frequency']
        pDD.dose = request.POST['dose']
        pDD.doseUnit = request.POST['doseUnit']
        pDD.directionDuration = request.POST['directionDuration']
        pDD.form = request.POST['form']
        pDD.additionalInstruc = request.POST['additionalInstruc']
        pDD.substance = request.POST['substance']
        pDD.safetyAmount = request.POST['safetyAmount']
        pDD.safetyDoseUnit = request.POST['safetyDoseUnit']
        pDD.safetyAllowedPer = request.POST['safetyAllowedPer']
        pDD.orderStatus = request.POST['orderStatus']
        pDD.orderDateDisc = request.POST['orderDateDisc']
        pDD.orderDateWritten = request.POST['orderDateWritten']
        pDD.authRepeat = request.POST['authRepeat']
        pDD.authValPer = request.POST['authValPer']
        pDD.dispInstruc = request.POST['dispInstruc']
        pDD.dispDescrip = request.POST['dispDescrip']
        pDD.dispAmount = request.POST['dispAmount']
        pDD.dispAmountUnits = request.POST['dispAmountUnits']
        pDD.dispDurution = request.POST['dispDurution']

        pDD.save()
        return render(request, 'hospital/patient_new_prescription.html', context=patientDict)
    return render(request, 'hospital/doctor_add_medicine.html', context=patientDict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def update_medicine_view(request,pk,mpk):
    medicine = models.PatientPrescriptionDetails.objects.all().filter(pk=mpk).first()
    patientDict ={
        'data' :medicine
    }
    if request.method=='POST':
        medicine.medicationItem = request.POST['medicationItem']
        medicine.frequency = request.POST['frequency']
        medicine.dose = request.POST['dose']
        medicine.doseUnit = request.POST['doseUnit']
        medicine.directionDuration = request.POST['directionDuration']
        medicine.form = request.POST['form']
        medicine.additionalInstruc = request.POST['additionalInstruc']
        medicine.substance = request.POST['substance']
        medicine.safetyAmount=request.POST['safetyAmount']
        medicine.safetyDoseUnit=request.POST['safetyDoseUnit']
        medicine.safetyAllowedPer=request.POST['safetyAllowedPer']
        medicine.orderStatus=request.POST['orderStatus']
        medicine.orderDateDisc=request.POST['orderDateDisc']
        medicine.orderDateWritten=request.POST['orderDateWritten']
        medicine.authRepeat=request.POST['authRepeat']
        medicine.authValPer=request.POST['authValPer']
        medicine.dispInstruc=request.POST['dispInstruc']
        medicine.dispDescrip=request.POST['dispDescrip']
        medicine.dispAmount=request.POST['dispAmount']
        medicine.dispAmountUnits=request.POST['dispAmountUnits']
        medicine.dispDurution=request.POST['dispDurution']
        medicine.save()
        return redirect('doctor-patient-search')
    return render(request,'hospital/doctor_update_medicine.html',context=patientDict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_medicine_view(request, pk, mpk):
    delete_dict = {
        'patientId': pk,
        'doctor': models.Doctor.objects.get(user_id=request.user.id),
    }
    medicine = models.PatientPrescriptionDetails.objects.all().filter(pk=mpk)
    if request.method == 'POST':
        medicine.delete()
        patient = models.Patient.objects.get(id=pk)
        assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
        pDD = models.PatientPrescriptionDetails.objects.all().filter(patientId=pk)
        patientDict = {
            'patientId': pk,
            'name': patient.get_name,
            'mobile': patient.mobile,
            'address': patient.address,
            'symptoms': patient.symptoms,
            'assignedDoctorName': assignedDoctor[0].first_name,
            'pDD': pDD,
            'todayDate': date.today(),
            'doctor': models.Doctor.objects.get(user_id=request.user.id),
        }
        return render(request, 'hospital/patient_new_prescription.html', context=patientDict)

    return render(request, 'hospital/doctor_delete_medicine.html', context=delete_dict)


@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def old_prescription_patient_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD = models.PatientPrescriptionDetails.objects.all().filter(
        patientId=pk).order_by('-date')

    date_list = []
    for m in pDD:
        if m.date not in date_list:
            date_list.append(m.date)

    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD': pDD,
        'date_list': date_list,
        'doctor': models.Doctor.objects.get(user_id=request.user.id),

    }

    return render(request, 'hospital/patient_old_prescription.html', context=patientDict)


# edited this -for patient

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_prescription_view(request):
    
    patient = models.Patient.objects.get(id=request.user.patient.id)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    pDD = models.PatientPrescriptionDetails.objects.all().filter(
        patientId=patient.id).order_by('-date')

    date_list = []
    for m in pDD:
        if m.date not in date_list:
            date_list.append(m.date)
    patientDict = {
        'patientId': patient.id,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'assignedDoctorName': assignedDoctor[0].first_name,
        'pDD': pDD,
        'patient': models.Patient.objects.get(user_id=request.user.id),
        'date_list': date_list
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
    patient = models.Patient.objects.get(id=request.user.patient.id)
    assignedDoctor = models.User.objects.all().filter(id=patient.assignedDoctorId)
    patientDict = {
        'patientId': patient.id,
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
        'patient': patient
    }

    return render(request, 'hospital/summary_patient.html', context=patientDict)
