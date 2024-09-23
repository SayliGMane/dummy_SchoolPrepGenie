from django.contrib.auth.models import User
from django.db import models
from apps.parent.models.parent import Class

class Teacher(models.Model):
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)  
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])