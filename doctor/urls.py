from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('my-home/', views.dr_home, name='dr-home'), 
    path('profile/', views.dr_profile, name='dr-pro'),
    path('patient/', views.dr_patient, name='dr-patient'),
    path('appointment/', views.my_appointments, name='my-appoint'),
    path('prescription/',views.prescription,name='prescrip'),
    path('schedule/',views.schedule,name='schedule'),
    path('holiday/',views.holiday,name='holiday'),
    path('dr_login/',views.dr_login,name='dr_login'),
    path('change_password/',views.chg_pwd,name='chg-pwd')
]