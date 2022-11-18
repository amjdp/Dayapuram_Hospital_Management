from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    admin_id = models.CharField(max_length = 50)
    admin_password = models.CharField(max_length = 20)

class Department(models.Model):
    department_name = models.CharField(max_length = 50)
    department_description = models.CharField(max_length = 1500)
    department_image = models.ImageField(upload_to = 'department/' , default="")
