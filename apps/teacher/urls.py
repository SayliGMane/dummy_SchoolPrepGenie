from django.urls import path
from . import views



app_name = 'teacher-urls'

urlpatterns = [
    path('', views.teacher_list_create, name='teacher-list-create'),
   
  
]
