
from rest_framework import serializers
from apps.parent.models.parent import Parent
from django.contrib.auth.models import User


class ParentSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
   
    parent_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
   
   
    
    class Meta:
        model = Parent
        fields = ['user', 'parent_name', 'username', 'email','gender', 'address','phone_number']
        read_only_fields = ['parent_name', 'username', 'email']

    def get_parent_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() if obj.user else None

    def get_username(self, obj):
        return obj.user.username if obj.user else None

    def get_email(self, obj):
        return obj.user.email if obj.user else None
    
    def get_gender(self, obj):
        return obj.user.gender if obj.user else None
    
    def validate_gender(self, value):
        """Validate that the gender is either 'M' or 'F'."""
        if value not in dict(Parent._meta.get_field('gender').choices):
            raise serializers.ValidationError("Invalid gender choice.")
        return value
        

    def create(self, validated_data):
        
        user = validated_data.pop('user')
        return Parent.objects.create(user=user, **validated_data)

    
    def update(self, instance, validated_data):
       
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.save()
                
        return instance