from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.student.serializer.student import StudentSerializer
from apps.student.models.student import Student




@api_view(['GET'])
def student_info(request):
    
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    return Response({'detail': 'Not authenticated'}, status=401)
   
 
