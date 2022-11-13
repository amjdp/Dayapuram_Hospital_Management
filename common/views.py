from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'common/homepage.html')

def masterpg(request):
    return render(request,'common/index.html')

def about(request):
    return render(request,'common/about.html')

def contact(request):
    return render(request,'common/contact.html')

def dept(request):
    return render(request,'common/department.html')

def service(request):
    return render(request,'common/service.html')

def login(request):
    return render(request,'common/login.html')

def dept_single(request):
    return render(request,'common/department-single.html')

def doc_1(request):
    return render(request,'common/doctor_1.html')

def doc_2(request):
    return render(request,'common/doctor_2.html')

def doc_3(request):
    return render(request,'common/doctor_3.html')

def doc_4(request):
    return render(request,'common/doctor_4.html')

def doc_5(request):
    return render(request,'common/doctor_5.html')

def doc(request):
    return render(request,'common/hms_doctor.html')

def documentation(request):
    return render(request,'common/documentation.html')

def blog_sidebar(request):
    return render(request,'common/blog-sidebar.html')

def blog_single(request):
    return render(request,'common/blog-single.html')

def login_b(request):
    return render(request,'common/login_base.html')

def login(request):
    return render(request,'common/login.html')

def demo(request):
    return render(request,'common/demo-dept.html')
