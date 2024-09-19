from django.contrib.auth.models import User
from django.db import models

class Teacher(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the Django User model
    subject = models.CharField(max_length=50, blank=True, null=True)        
    years_of_experience = models.IntegerField(blank=True, null=True)         
    
    def __str__(self):
        return f"Teacher: {self.user.username}"



