from django.urls import path
from . import views



app_name = 'parent-urls'

urlpatterns = [
    path('', views.parent_list_create, name='parent-list-create'),
   
  
]
