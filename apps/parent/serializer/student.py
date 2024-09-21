
from rest_framework import serializers
from apps.parent.models.student import Student
from .classs import ClassSerializer

class StudentSerializer(serializers.ModelSerializer):
    
    class_info = ClassSerializer(source='class_id') 
    
    class Meta:
        model = Student
        fields = ['id','first_name', 'last_name', 'age', 'class_info', 'gender']

