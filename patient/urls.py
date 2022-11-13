from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('home', views.p_home, name='phome'),
    path('appointment', views.appointment, name='appointment'),
    path('confirmation', views.confirmation, name='confirm'),
    path('online-booking', views.online_booking, name='online'),
    path('my-bookings', views.my_bookings, name='bookings'),
    path('my-prescriptions', views.prescriptions, name='prescriptions'),
    path('change-password', views.chpass, name='chg-pwd'),
    path('profile', views.pt_profile, name='my-pro'),
    path('login', views.pt_login, name='pt_login'),
    path('register', views.reg, name='pt_reg'),
    path('pt', views.hello, name='hello'),
    path('appointment_1', views.app, name='apt'),
    path('edit_profile', views.edit, name='edit_pt'),
    path('new_appt', views.appt, name='new_apt'),
    path('appointment-1', views.appt_1, name='appointment_1'),
    path('appointment-2', views.appt_2, name='appointment_2'),
    path('appointment-3', views.appt_3, name='appointment_3'),
     path('booking-confirmation', views.appt_4, name='appointment_4')
]
