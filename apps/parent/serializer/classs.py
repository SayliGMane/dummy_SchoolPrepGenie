from rest_framework import serializers
from apps.parent.models.parent import Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'academic_year_start', 'academic_year_end', 'grade']
