from django.urls import path
from . import views

app_name = 'teacher-urls'
urlpatterns = [


    path('registration/', views.teacher_list, name='teacher_list_create'),
  
     
    
]    