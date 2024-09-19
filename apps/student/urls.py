from django.urls import path
from . import views



app_name = 'student-urls'

urlpatterns = [
    path('', views.student_list_create, name='student-list-create'),
   
  
]
