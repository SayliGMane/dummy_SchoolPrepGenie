from rest_framework import serializers
from apps.teacher.models.lunchmenu import LunchMenu  # Import the model

class LunchMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchMenu
        fields = ['Week', 'Day', 'Menu']  # List of fields you want to expose in the API
