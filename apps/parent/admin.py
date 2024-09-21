from django.contrib import admin
from .models.parent import Parent,Class
from .models.student import Student


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
    
    

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'age',
        'gender',
        'class_name',
        'parent_full_name'
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Student Name'

    def class_name(self, obj):
        return obj.class_id.class_name  
    class_name.short_description = 'Class'

    def parent_full_name(self, obj):
            return f"{obj.parent.user.first_name} {obj.parent.user.last_name}" if obj.parent else 'N/A'
    parent_full_name.short_description = 'Parent Name'

    
    
admin.site.register(Class,ClassAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Student,StudentAdmin)