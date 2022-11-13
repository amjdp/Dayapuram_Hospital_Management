from django.urls import path
from . import views

app_name = 'receptionist'

urlpatterns = [
    path('my-home/', views.reception_home, name='home'),
    path('registration/', views.regn, name='reg'),
    path('appointments/', views.app, name='app-list'),
    path('patients/', views.pt_search, name='search')     
]