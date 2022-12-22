from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    admin_id = models.CharField(max_length = 50)
    admin_password = models.CharField(max_length = 20)

class Department(models.Model):
    department_name = models.CharField(max_length = 50)
    department_description = models.CharField(max_length = 1500)
    department_image = models.ImageField(upload_to = 'department/' , default="")

class Doctor(models.Model):
    doctor_name = models.CharField(max_length = 50)   # varchar(25)
    doctor_email = models.CharField(max_length = 50)
    doctor_password = models.CharField(max_length = 30)
    doctor_contact_no = models.CharField(max_length = 30)
    doctor_qualification = models.CharField(max_length = 30)
    doctor_experience = models.IntegerField()
    consultation_fees = models.CharField(max_length = 10)    
    doctor_profile_picture = models.ImageField(upload_to = 'doctor/')
    doctor_department_id = models.ForeignKey(Department,on_delete = models.CASCADE)

