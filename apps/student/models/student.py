from django.db import models
from apps.parent.models.parent import Parent,Class
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Student(models.Model):
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)  
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)  
    first_name = models.CharField(max_length=100, null=True, blank=True)  
    last_name = models.CharField(max_length=100, null=True, blank=True)  
   

    def set_password(self, raw_password):
        self.password = make_password(raw_password) 
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Hash the password before saving
            
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"