from django.db import models
from .parent import Parent,Class

class Student(models.Model):
    
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)  
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"