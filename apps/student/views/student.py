from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from apps.student.serializer.student import StudentSerializer
from apps.student.models.student import Student
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication
import secrets


@api_view(['GET'])
def student_info(request):
    
    print(f"Authorization header: {request.headers.get('Authorization')}")
    
    student = request.user
    print(f"Authenticated student: {student.username}")

   
    serializer = StudentSerializer(student)
    
    return Response(serializer.data)
   
    #token = request.headers.get('Authorization')

    # Ensure token is provided
   # if not token:
      #  return Response({"error": "Token is required."}, status=403)

    # Try to get the student based on the token
   # try:
     #   student = Student.objects.get(token=token)
   # except Student.DoesNotExist:
      #  return Response({"error": "Invalid token."}, status=403)

    # Serialize the student data
   # serializer = StudentSerializer(student)
   # return Response(serializer.data)
   
   
