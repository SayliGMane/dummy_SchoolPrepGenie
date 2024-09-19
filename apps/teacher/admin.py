from django.contrib import admin
from apps.student.models.student import Class
from apps.teacher.models.teacher import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','username','gender', 'get_class_name')
    
    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'

  

    def get_class_name(self, obj):
        return obj.class_id.class_name if obj.class_id else 'No Class'
    get_class_name.short_description = 'Class Name'
    

admin.site.register(Teacher, TeacherAdmin)



