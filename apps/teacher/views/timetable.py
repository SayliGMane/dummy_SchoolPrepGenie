
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.teacher.models.teacher import Teacher
#from apps.teacher.serializer.teacher import TeacherSerializer
from apps.teacher.serializer.timetable import TimeTableSerializer
from apps.teacher.models.timetable import TimeTable




@api_view(['POST'])
def create_timetable(request):
    data = request.data.copy()

    # Get the teacher associated with the logged-in user
    teacher = request.user.teacher
    data['teacher'] = teacher.id
    
    # Check if a timetable already exists for the teacher and class
    class_id = data.get('class_id')
    existing_timetable = TimeTable.objects.filter(teacher=teacher, class_id=class_id).first()
    print (existing_timetable.data)
    if not existing_timetable:
        return Response(
            {"error": "Timetable for this class already exists."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # If no timetable exists, create a new one
    serializer = TimeTableSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    