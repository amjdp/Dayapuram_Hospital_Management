from django.shortcuts import render

# Create your views here.
def reception_home(request):
    return render(request,'receptionist/rec_home.html')

def regn(request):
    return render(request,'receptionist/registration.html')

def app(request):
    return render(request,'receptionist/appointments-list.html')

def pt_search(request):
    return render(request,'receptionist/patient_search.html')