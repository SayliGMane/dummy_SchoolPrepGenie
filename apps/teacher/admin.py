from django.contrib import admin
from apps.teacher.models.teacher import Teacher
from apps.teacher.models.timetable import TimeTable


#update same for timetable
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'gender', 'class_name')

    def username(self, obj):
        return obj.user.username  

    def first_name(self, obj):
        return obj.user.first_name  

    def last_name(self, obj):
        return obj.user.last_name  
    def class_name(self, obj):
        return obj.class_id.class_name  

    username.admin_order_field = 'user__username'  
    first_name.admin_order_field = 'user__first_name'  
    last_name.admin_order_field = 'user__last_name'  
    class_name.admin_order_field = 'class_id__class_name' 

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TimeTable)
