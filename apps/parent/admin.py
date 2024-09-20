from django.contrib import admin
from .models.parent import Parent
from apps.student.models.student import Student


class StudentInline(admin.TabularInline):  
    model = Student
    extra = 1 

class ParentAdmin(admin.ModelAdmin):
    
    list_display = ('id','full_name','username','gender','address','phone_number','email','date_of_join','student_names')
    
    inlines = [StudentInline] 

    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def email(self,obj):
        return obj.user.email
    
    def date_of_join(self, obj):
        return obj.user.date_joined
    
    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'
    
    def student_names(self, obj):
        
        students = obj.children.all()
        return ", ".join([f"{student.first_name} {student.last_name}" for student in students]) if students else "No students"
    student_names.short_description = 'Students'


admin.site.register(Parent,ParentAdmin)