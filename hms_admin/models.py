from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    admin_id = models.CharField(max_length = 50)
    admin_password = models.CharField(max_length = 20)