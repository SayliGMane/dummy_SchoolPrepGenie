from rest_framework import serializers
from apps.student.models.student import Student
from apps.student.models.student import Class
from apps.parent.models.parent import Parent



class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name']

class StudentSerializer(serializers.ModelSerializer):
    
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(),  write_only=True)
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all(), write_only=True, required=False)
    

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'class_id', 'gender', 'parent']  
        
    def get_class_id(self, obj):
        return obj.class_id.class_name if obj.class_id else None

    def get_parent(self, obj):
        from apps.parent.serializer.parent import ParentSerializer
        if obj.parent:
            return ParentSerializer(obj.parent).data
        return None

    def to_representation(self, instance):
        
        representation = super().to_representation(instance)
        representation['class_name'] = instance.class_id.class_name if instance.class_id else None
        
        parent_data = self.get_parent(instance)
        if parent_data:
            representation['parent_name'] = parent_data.get('parent_name', 'No Parent')
            representation['parent_username'] = parent_data.get('username', 'No Username')
            representation['parent_email'] = parent_data.get('email', 'No Email')
            representation['contact_number'] = parent_data.get('phone_number','No Phone Number')
        
        return representation
    
    def create(self, validated_data):
        class_id = validated_data.pop('class_id')
        parent = validated_data.pop('parent', None)
        student = Student.objects.create(class_id=class_id, parent=parent, **validated_data)
        return student

    def update(self, instance, validated_data):
        class_id = validated_data.pop('class_id', None)
        parent = validated_data.pop('parent', None)
        if class_id:
            instance.class_id = class_id
        if parent:
            instance.parent = parent
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance