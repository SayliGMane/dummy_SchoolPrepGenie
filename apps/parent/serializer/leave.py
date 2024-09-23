from rest_framework import serializers
from apps.parent.models.leave import Leave
from apps.parent.models.parent import Parent
from apps.student.models.student import Student

class LeaveSerializer(serializers.ModelSerializer):
    
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    
    parent_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    

    class Meta:
        model = Leave
        fields = ['id','parent','parent_name','student','student_name','class_name','leave_type', 'status', 'leave_description', 'start_date', 'end_date']
        read_only_fields = ['status'] 
        
    def get_parent_name(self, obj):
        return obj.parent.user.first_name + " " + obj.parent.user.last_name

    def get_student_name(self, obj):
        return obj.student.first_name + " " + obj.student.last_name  
    
    
    def get_class_name(self, obj):
        return obj.student.class_id.class_name
    
    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be greater than or equal to start date.")
        return data    

    def create(self, validated_data):
        
        leave_instance = Leave.objects.create(**validated_data)
        return leave_instance