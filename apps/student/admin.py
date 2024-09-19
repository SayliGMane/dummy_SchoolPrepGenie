from django.contrib import admin
from .models.student import Student,Class

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'class_id', 'gender', 'parent_name')

    def parent_name(self, obj):
        if obj.parent:
            user = obj.parent.user
            return f"{user.first_name} {user.last_name}" if user else 'No Parent'
        return 'No Parent'

    parent_name.short_description = 'Parent Name'

admin.site.register(Student, StudentAdmin)
admin.site.register(Class)