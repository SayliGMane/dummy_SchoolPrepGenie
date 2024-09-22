from django.contrib import admin
from .models.parent import Parent,Class
from apps.student.models.student import Student


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
    
    


    
admin.site.register(Class,ClassAdmin)
admin.site.register(Parent,ParentAdmin)
