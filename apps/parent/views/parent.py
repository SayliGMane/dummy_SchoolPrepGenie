
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from apps.parent.models.parent import Parent
from apps.parent.serializer import ParentSerializer
from apps.user.serializer import UserSerializer
from apps.student.serializer import StudentSerializer


@api_view(['GET', 'POST'])
def parent_list_create(request):
    
  
    """
    List all parents or create a new parent.
    """
    if request.method == 'GET':
        # List all parents
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        
        user_data = request.data.get('user', {})
        
        parent_data = {
            'phone_number': request.data.get('phone_number'),
            'address': request.data.get('address'),
            'gender': request.data.get('gender')
        }
        
         
        user_serializer = UserSerializer(data=user_data)
        
        if user_serializer.is_valid():
            user = user_serializer.save()

           
            parent_data['user'] = user.id
            parent_serializer = ParentSerializer(data=parent_data)
            
            if parent_serializer.is_valid():
                parent = parent_serializer.save()
                return Response(parent_serializer.data, status=status.HTTP_201_CREATED)
            else:
              
                return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  