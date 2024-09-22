
from rest_framework import serializers
from apps.parent.models.student import Student
from .classs import ClassSerializer
from django.contrib.auth.models import User
from apps.parent.models.parent import Class

class StudentSerializer(serializers.ModelSerializer):
    
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())  # For input
    class_info = ClassSerializer(source='class_id', read_only=True)  # For output
  

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'class_id', 'class_info', 'gender']
  