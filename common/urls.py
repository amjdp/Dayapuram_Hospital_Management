from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.home, name='com-home'),
    path('master_page', views.masterpg, name='master'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.dept, name='depts'),
    path('services/', views.service, name='services'),
    path('login/', views.login, name='login'),
    path('dept-single/', views.dept_single, name='dept-single'),
    path('doctor-single/', views.doctor_single, name='dr-single'),
    path('doctor/', views.doctor, name='dr'),
    path('login_base/', views.login_common, name='log_b'),
    path('login/', views.login, name='login'),
]