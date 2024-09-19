from rest_framework import serializers
from apps.teacher.models.teacher import Teacher
from apps.student.serializer.student import ClassSerializer
from django.contrib.auth.models import User
from apps.student.models.student import Class


class TeacherSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
   
    teacher_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())   
    class_name = serializers.SerializerMethodField()
    
        
    class Meta:
        model = Teacher
        fields = ['user', 'teacher_name', 'username','gender','class_id','class_name']
        read_only_fields = ['teacher_name', 'username','class_name']
        
    def get_teacher_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() if obj.user else None

    def get_username(self, obj):
        return obj.user.username if obj.user else None
    
    def get_gender(self, obj):
        return obj.user.gender if obj.user else None
    
    def get_class_name(self, obj):
        return obj.class_id.class_name if obj.class_id else 'No Class'
    
    def create(self, validated_data):
        
        user = validated_data.pop('user')
        class_data = validated_data.pop('class_id', None)
        
        teacher = Teacher.objects.create(user=user, class_id=class_data, **validated_data)
      
        return teacher

    def update(self, instance, validated_data):
        
        instance.gender = validated_data.get('gender', instance.gender)
        class_data = validated_data.get('class_id', instance.class_id)
        
        if class_data is not None:
            instance.class_id = class_data
        
        instance.save()
        return instance
