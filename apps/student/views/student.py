from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.student.models.student import Student
from apps.student.serializer import StudentSerializer

@api_view(['GET', 'POST'])
def student_list_create(request):
    """
    List all students, or create a new student.
    """
    if request.method == 'GET':
        # Retrieve and return all students
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
