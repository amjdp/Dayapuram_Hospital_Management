from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('my-home/', views.staff_home, name='st-home'),
    path('registration/', views.regn, name='pt-reg'),
    path('appointments/', views.app, name='app-list'),
    path('patient_search/', views.pt_search, name='pt-search'),  
    path('filter/', views.filter, name='filter'),
    path('staff/', views.staff_list, name = 'staff-list')
]
