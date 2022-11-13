from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'hms_admin/admin_home.html')

def add_admin(request):
    return render(request,'hms_admin/add_admin.html')

def view_admin(request):
    return render(request,'hms_admin/view_admin.html')

def adm_prof(request):
    return render(request,'hms_admin/admin_profile.html')

def chg_pwd(request):
    return render(request,'hms_admin/change_password.html')

def view_app(request):
    return render(request,'hms_admin/view_appointments.html')

def add_dr(request):
    return render(request,'hms_admin/add_doctor.html')

def view_dr(request):
    return render(request,'hms_admin/view_doctor.html')

def view_report(request):
    return render(request,'hms_admin/view_report.html')

def add_dr(request):
    return render(request,'hms_admin/add_doctor.html')

def add_pt(request):
    return render(request,'hms_admin/add_patient.html')

def view_pt(request):
    return render(request,'hms_admin/view_patient.html')

def add_dt(request):
    return render(request,'hms_admin/add_dept.html')

def view_dt(request):
    return render(request,'hms_admin/view_dept.html')

def admin_login(request):
    return render(request,'hms_admin/admin_login.html')

