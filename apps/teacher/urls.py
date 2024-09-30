from django.urls import path
from . import views

app_name = 'teacher-urls'
urlpatterns = [


    path('registration/', views.teacher_list, name='teacher_list_create'),
    path('create/timetable/', views.create_timetable, name='create_timetable'),
    path('lunchmenu/', views.lunch_menu_view, name='lunch_menu'),
  
     
    
]    