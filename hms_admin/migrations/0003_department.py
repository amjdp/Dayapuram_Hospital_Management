# Generated by Django 4.1.3 on 2022-11-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms_admin', '0002_rename_admin_passwrod_adminlogin_admin_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
                ('department_description', models.CharField(max_length=1500)),
            ],
        ),
    ]
