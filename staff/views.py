from django.shortcuts import render

# Create your views here.
def staff_home(request):
    return render(request,'staff/staff_home.html')

def regn(request):
    return render(request,'staff/registration.html')

def app(request):
    return render(request,'staff/appointments.html')

def pt_search(request):
    return render(request,'staff/patient_search.html')