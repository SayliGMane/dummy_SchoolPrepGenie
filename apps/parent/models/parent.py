from django.core.validators import RegexValidator 
from django.db import models


class Parent(models.Model):
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d{9}$', message="Contact number should be 9 digits.")],
        blank=True,  
        null=True
    )
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')],blank=True, null=True, default='M')
    address = models.CharField(max_length=255, blank=True, null=True)      
    
    class Meta:
        verbose_name_plural = 'Parent'
        db_table = "parent"

        constraints = [
            
            models.UniqueConstraint(fields=['phone_number'], name='unique_contact_number'),
                
        ]

        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Class(models.Model):
    
    class_name = models.CharField(max_length=100)
    academic_year_start = models.IntegerField()
    academic_year_end = models.IntegerField()
    grade = models.IntegerField()

    def __str__(self):
        return self.class_name

