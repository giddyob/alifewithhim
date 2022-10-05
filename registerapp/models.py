from django.db import models

# Create your models here.
class Registration(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=15)
    user_email = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=50)
    user_mode_of_info = models.CharField(max_length=50)
    user_first_time = models.CharField(max_length=50)
    user_residence = models.CharField(max_length=100)
    user_arrival_day = models.CharField(max_length=50)
    
    