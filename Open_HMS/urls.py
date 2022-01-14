"""Open_HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('doctorclick', views.doctorclick_view),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),
    path('patientclick', views.patientclick_view),
    path('patientsignup', views.patient_signup_view),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),

    path('doctor-patient-search', views.doctor_patient_search_view,name='doctor-patient-search'),
    #path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),

    path('patient-prescription/<int:pk>', views.prescription_patient_view,name='patient-prescription'),
    path('patient-prescription', views.patient_prescription_view,name='patient-prescription'),
    path('patient-summary/<int:pk>', views.summary_patient_view,name='patient-summary'),

]