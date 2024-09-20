from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from apps.parent.models.parent import Parent


class Class(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}) {self.class_name}"
    

class Student(models.Model):
    
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    first_name = models.CharField(max_length=100,default='Unknown')
    last_name = models.CharField(max_length=100,default='Unknown')
    age = models.PositiveIntegerField(default=0)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students',default=1,null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')],default='M')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name', 'age', 'class_id'], name='unique_student_entry')
        ]
    

    def __str__(self):
        class_name = self.class_id.class_name if self.class_id else 'No Class'
     
        return (f"Name: {self.first_name} {self.last_name}, "
                f"Age: {self.age}, "
                f"Class: {class_name}, "
                f"Gender: {self.get_gender_display()}, "
                )