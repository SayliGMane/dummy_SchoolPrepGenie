from django.contrib import admin
from .models.parent import Parent,Class
from apps.parent.models.leave import Leave


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id','class_name', 'academic_year_start', 'academic_year_end', 'grade')

class ParentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_username', 
        'user_first_name', 
        'user_last_name', 
        'user_email', 
        'address', 
        'phone_number', 
        'gender',  
        'user_date_joined'
    )

    def user_username(self, obj):
        return obj.user.username
    user_username.admin_order_field = 'user__username'
    user_username.short_description = 'Username'

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.admin_order_field = 'user__first_name'
    user_first_name.short_description = 'First Name'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.admin_order_field = 'user__last_name'
    user_last_name.short_description = 'Last Name'

    def user_email(self, obj):
        return obj.user.email
    user_email.admin_order_field = 'user__email'
    user_email.short_description = 'Email'
    
    def user_date_joined(self, obj):
        return obj.user.date_joined  
    user_date_joined.admin_order_field = 'user__date_joined'
    user_date_joined.short_description = 'Date Joined'
    
    
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_parent_name', 'get_student_name', 'get_class_name', 'leave_type', 'status', 'leave_description', 'start_date', 'end_date')

    def get_parent_name(self, obj):
        return f"{obj.parent.user.first_name} {obj.parent.user.last_name}"  

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}" 

    def get_class_name(self, obj):
        return obj.student.class_id.class_name 

    get_parent_name.short_description = 'Parent Name'
    get_student_name.short_description = 'Student Name'
    get_class_name.short_description = 'Class Name'


    
admin.site.register(Class,ClassAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Leave,LeaveAdmin)
