from django.db import models
from apps.teacher.models.teacher import Teacher
from apps.parent.models.parent import Class
from django.contrib.auth.models import User

class TimeTable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    timetable_content = models.JSONField() 
    
    def __str__(self):
        return f"Timetable for {self.teacher.user.username} - Class {self.class_id}"
