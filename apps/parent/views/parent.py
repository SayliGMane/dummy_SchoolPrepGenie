
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.parent.models.parent import Parent
from apps.parent.serializer.parent import ParentSerializer
from apps.student.models.student import Student
from apps.student.serializer.student import StudentSerializer

@api_view(['GET', 'POST'])
def parent_list(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def student_info(request):
   
    #if not request.user.is_authenticated:
       # return Response({'detail': 'Authentication required.'}, status=401)

   
    students = Student.objects.filter(parent__user=request.user)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)    