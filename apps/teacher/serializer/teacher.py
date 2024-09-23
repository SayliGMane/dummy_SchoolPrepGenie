from rest_framework import serializers
from apps.user.serializer.user import UserSerializer
from apps.teacher.models.teacher import Teacher
from apps.parent.models.parent import Class
from apps.parent.serializer.classs import ClassSerializer

class TeacherSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()  

    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())  
    
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'gender', 'class_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  
        class_id = validated_data.pop('class_id') 

      
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()  
       
       
        teacher = Teacher.objects.create(user=user, class_id=class_id, **validated_data)

        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = UserSerializer(instance.user, data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

        instance.gender = validated_data.get('gender', instance.gender)
        instance.class_id_id = validated_data.get('class_id', instance.class_id_id)  #
        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['class_id'] = ClassSerializer(instance.class_id).data  # Expand class_id details
        return representation