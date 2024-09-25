# # teacher/serializers/timetable.py
from rest_framework import serializers
from apps.teacher.models.timetable import TimeTable

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ['id', 'teacher', 'class_id', 'timetable_content']
