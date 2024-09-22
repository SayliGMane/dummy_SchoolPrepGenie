
from rest_framework import serializers
from apps.student.models.student import Student
from apps.parent.serializer.classs import ClassSerializer
from django.contrib.auth.models import User
from apps.parent.models.parent import Class
from django.contrib.auth.hashers import check_password

class StudentSerializer(serializers.ModelSerializer):
    
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())  # For input
    class_info = ClassSerializer(source='class_id', read_only=True)  # For output
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'class_id', 'class_info', 'gender','username','password']
  
    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.set_password(password)  # Save the hashed password
        student.save()
        return student
    
class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            student = Student.objects.get(username=data['username'])
        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password.")

        if not check_password(data['password'], student.password):
            raise serializers.ValidationError("Invalid username or password.")
        
        return data    
    