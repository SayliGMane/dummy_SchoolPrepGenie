from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.parent.models.leave import Leave
from apps.parent.serializer.leave import LeaveSerializer
from apps.student.models.student import Student
from apps.parent.models.parent import Parent



@api_view(['GET', 'POST'])
def parent_leave_list_create(request):
    if request.method == 'GET':
        leaves = Leave.objects.all()
        serializer = LeaveSerializer(leaves, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
       
        parent_id = request.data.get('parent_id')
        student_id = request.data.get('student_id')
        
        print("Found Parent:", parent_id,student_id)
        
        try:
            parent = Parent.objects.get(id=parent_id)
           
        except Parent.DoesNotExist:
            return Response({'error': 'User has no parent associated.'}, status=status.HTTP_400_BAD_REQUEST)

        
        
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = {
            'leave_type': request.data.get('leave_type'),
            'leave_description': request.data.get('leave_description'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'parent': request.data.get('parent_id'),
            'student': request.data.get('student_id')
        }
        
        print('validated data-----------',validated_data)

        serializer = LeaveSerializer(data=validated_data)
        if serializer.is_valid():
            leave_instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)