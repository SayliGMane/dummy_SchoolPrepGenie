
from django.urls import path
from . import views



app_name = 'student-urls'
urlpatterns = [


 
    path('info/', views.student_info, name='student_info'),
    path('login/', views.student_login, name='student_login'), 
    
]    