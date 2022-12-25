from django.urls import path
from . import views

app_name = 'hms_admin'

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('view_appointments',views.view_app,name='app_view'),
    path('view_report',views.view_report,name='view_report'),
    path('add_doctor',views.add_dr,name='add_dr'),
    path('view_doctor',views.view_dr,name='view_dr'),
    path('view_patient',views.view_patient,name='view_pt'),
    path('add_department',views.add_department,name='add_dt'),
    path('view_department',views.view_dt,name='view_dt'),
    path('change_password',views.chg_pwd,name='chg_pwd'),
    path('admin_login',views.admin_login,name='login'),
    path('add_staff',views.add_staff,name='add_staff'),
    path('view_staff',views.view_staff,name='view_staff'),
    path('admin_logout',views.admin_logout,name='admin_logout')
]