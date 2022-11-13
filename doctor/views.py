from django.shortcuts import render

# Create your views here.
def dr_home(request):
    return render(request,'doctor/doctor_home.html')

def dr_profile(request):
    return render(request,'doctor/dr_profile.html')

def dr_patient(request):
    return render(request,'doctor/patient.html')

def my_appointments(request):
    return render(request,'doctor/my_appointments.html')

def prescription(request):
    return render(request,'doctor/prescription.html')

def schedule(request):
    return render(request,'doctor/schedule.html')

def holiday(request):
    return render(request,'doctor/holiday.html')

def dr_login(request):
    return render(request,'doctor/dr_login.html')

def chg_pwd(request):
    return render(request,'doctor/change_pwd.html')
