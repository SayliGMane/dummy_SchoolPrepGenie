import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.teacher.models.teacher import Teacher
from apps.teacher.serializer.teacher import TeacherSerializer
from apps.user.serializer import UserSerializer



@api_view(['GET', 'POST'])
def teacher_list_create(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        
        user_data = request.data.get('user', {})
        
        password = user_data.pop('password', None)
        
        teacher_data = {
            
           
            'gender': request.data.get('gender'),
            'class_id': request.data.get('class_id') 
        }
        
        user_serializer = UserSerializer(data=user_data)
        
        if user_serializer.is_valid():
            user = user_serializer.save()
            if password:  
                user.set_password(password)
                user.save()

            teacher_data['user'] = user.id
            teacher_serializer = TeacherSerializer(data=teacher_data)
        
            if teacher_serializer.is_valid():
                teacher = teacher_serializer.save()
             
                return Response(teacher_serializer.data, status=status.HTTP_201_CREATED)
            else:
             
                return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
         
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    