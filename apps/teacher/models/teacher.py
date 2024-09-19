from django.contrib.auth.models import User
from django.db import models
from apps.student.models.student import Class



class Teacher(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='teacher',default=1,null=True, blank=True)        
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')],blank=True, null=True, default='F')       
    
    
    class Meta:
        verbose_name_plural = 'Teachers'
        db_table = "teacher"

        constraints = [
            # Ensure that each user is linked to only one teacher
            models.UniqueConstraint(fields=['user'], name='unique_user_teacher'),
            # Ensure that combination of class_id and gender is unique 
            models.UniqueConstraint(fields=['class_id', 'gender'], name='unique_class_gender_teacher')
        ]

        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['class_id'])
        ]
    
    def __str__(self):
        class_name = self.class_id.class_name if self.class_id else 'No Class'
        return f"{self.user.username} {self.user.first_name} {self.user.last_name} {self.gender} {class_name}"



