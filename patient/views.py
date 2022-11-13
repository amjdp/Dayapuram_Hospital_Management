from django.shortcuts import render

# Create your views here.
def p_home(request):
    return render(request,'patient/patient_home.html')

def appointment(request):
    return render(request,'patient/appointment.html')

def confirmation(request):
    return render(request,'patient/confirmation.html')

def online_booking(request):
    return render(request,'patient/online_booking.html')

def my_bookings(request):
    return render(request,'patient/my_bookings.html')

def prescriptions(request):
    return render(request,'patient/prescriptions.html')

def chpass(request):
    return render(request,'patient/change-password.html')

def pt_profile(request):
    return render(request,'patient/patient_profile.html')

def pt_profile(request):
    return render(request,'patient/pt-profile.html')

def pt_login(request):
    return render(request,'patient/pt_login.html')

def reg(request):
    return render(request,'patient/register.html')
    
def hello(request):
    return render(request,'patient/hello.html')

def app(request):
    return render(request,'patient/appointment_new.html')

def edit(request):
    return render(request,'patient/edit_profile.html')

def appt(request):
    return render(request,'patient/new_appt.html')

def appt_1(request):
    return render(request,'patient/appt_1.html')

def appt_2(request):
    return render(request,'patient/appt_2.html')

def appt_3(request):
    return render(request,'patient/appt_3.html')

def appt_4(request):
    return render(request,'patient/appt_4.html')

    