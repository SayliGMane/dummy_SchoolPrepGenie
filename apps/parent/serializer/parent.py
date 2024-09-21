from rest_framework import serializers
from apps.parent.models.parent import Parent,Class
from apps.parent.models.student import Student
from apps.user.serializer.user import UserSerializer
from .student import StudentSerializer



class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    children = StudentSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['user', 'address', 'phone_number', 'gender', 'children']

    def create(self, validated_data):
        children_data = validated_data.pop('children')
        user_data = validated_data.pop('user')

        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        parent = Parent.objects.create(user=user, **validated_data)

        for child_data in children_data:
            class_id = child_data.pop('class_id')
            try:
                
                Student.objects.create(parent=parent, class_id=class_id, **child_data)
            except Class.DoesNotExist:
                raise serializers.ValidationError({"children": {child_data["first_name"]: "Invalid class_id."}})

        return parent

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['children'] = StudentSerializer(instance.children.all(), many=True).data
        return representation