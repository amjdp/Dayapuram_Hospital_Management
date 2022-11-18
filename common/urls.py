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
    path('blog-sidebar/', views.blog_sidebar, name='blog-sb'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('dept-single/', views.dept_single, name='dept-single'),
    path('doctor-1/', views.doc_1, name='dr-1'),
    path('doctor-2/', views.doc_2, name='dr-2'),
    path('doctor-3/', views.doc_3, name='dr-3'),
    path('doctor-4/', views.doc_4, name='dr-4'),
    path('doctor-5/', views.doc_5, name='dr-5'),
    path('doctor/', views.doc, name='dr'),
    path('documentation/', views.documentation, name='doc'),
    path('login_base/', views.login_b, name='log_b'),
    path('login/', views.login, name='login'),
    path('heartcare',views.heartcare, name = 'heart'),
    path('womencare',views.womencare, name = 'women'),
    path('childcare',views.childcare, name = 'child'),
    path('neuroscience',views.neuroscience, name = 'neuro'),
    path('liver',views.liver, name = 'liver'),
    path('orthopaedics',views.orthopaedics, name = 'ortho'),
    path('renalcare',views.renalcare, name = 'renal'),
    path('endocrine',views.endocrine, name = 'endocrine'),
    path('psychiatry',views.psychiatry, name = 'psychiatry'),
    path('oncology',views.oncology, name = 'oncology'),
    path('anaesthesiology',views.anaesthesiology, name = 'anaesthesiology'),
    path('radiology',views.radiology, name = 'radiology'),
    path('dermatology',views.dermatology, name = 'dermatology'),
    path('bloodbank',views.bloodbank, name = 'bloodbank'),
    path('demo/', views.demo, name='demo')   
]