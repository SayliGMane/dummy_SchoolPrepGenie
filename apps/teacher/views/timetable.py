
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.teacher.models.teacher import Teacher
#from apps.teacher.serializer.teacher import TeacherSerializer
from apps.teacher.serializer.timetable import TimeTableSerializer
from apps.teacher.models.timetable import TimeTable



# @api_view(['GET', 'POST'])
# def timetable_list(request):
#     if request.method == 'GET':
#         timetables = TimeTable.objects.all()
#         serializer = TimeTableSerializer(timetables, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TimeTableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_timetable(request):

    data = request.data.copy()
    
   
    teacher = request.user.teacher 
    data['teacher'] = teacher.id
    
    serializer = TimeTableSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)