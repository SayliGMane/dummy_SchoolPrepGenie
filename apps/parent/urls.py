from django.urls import path
from . import views


app_name = 'parent-urls'
urlpatterns = [


    path('registration/', views.parent_list, name='parent_list_create'),
    path('student/info/', views.student_info, name='student_info'),
     
    
]    