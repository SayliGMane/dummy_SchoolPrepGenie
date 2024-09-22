from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from apps.student.serializer.student import StudentLoginSerializer,StudentSerializer
from apps.student.models.student import Student
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def student_login(request):
    
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        # Get the validated data
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        # Retrieve the student instance
        try:
            student = Student.objects.get(username=username)
        except Student.DoesNotExist:
            return Response({"non_field_errors": ["Invalid username or password."]}, status=status.HTTP_400_BAD_REQUEST)

        # Check the password
        if not check_password(password, student.password):
            return Response({"non_field_errors": ["Invalid username or password."]}, status=status.HTTP_400_BAD_REQUEST)
        
        # If login is successful
        return Response({"message": "Login successful", "student_id": student.id}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_info(request):
   
    #if not request.user.is_authenticated:
       # return Response({'detail': 'Authentication required.'}, status=401)

   
    student = request.user  # Assuming you are using the User model for authentication
    student_data = Student.objects.filter(user=student)  # Fetch the student related to the user
    serializer = StudentSerializer(student_data, many=True)
    return Response(serializer.data)   