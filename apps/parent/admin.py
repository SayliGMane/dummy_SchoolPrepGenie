from django.contrib import admin
from .models.parent import Parent

class ParentAdmin(admin.ModelAdmin):
    
    list_display = ('id','full_name','username','gender','address','phone_number','email','date_of_join')

    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def email(self,obj):
        return obj.user.email
    
    def date_of_join(self, obj):
        return obj.user.date_joined
    
    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'


admin.site.register(Parent,ParentAdmin)