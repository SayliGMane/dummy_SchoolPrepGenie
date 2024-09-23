
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.parent.models.parent import Parent
from apps.parent.serializer.parent import ParentSerializer
from apps.student.models.student import Student
from apps.student.serializer.student import StudentSerializer
from django.contrib.auth.models import User
from apps.parent.models.parent import Class

@api_view(['GET', 'POST'])
def parent_list(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
       
        parent_data = request.data.get('user')
        children_data = request.data.get('children')
        gender = request.data.get('gender')
        address = request.data.get('address')
        phone_number = request.data.get('phone_number')

       
        parent_user = User.objects.create_user(
            username=parent_data['username'],
            password=parent_data['password'],
            first_name=parent_data.get('first_name', ''),
            last_name=parent_data.get('last_name', ''),
            email=parent_data['email']
        )
        print("Created Parent User:", parent_user.username)

       
        parent = Parent.objects.create(user=parent_user,address=address,phone_number=phone_number)
        print("Created Parent:", parent.user.get_full_name())

        students = []

        for child_data in children_data:
           
            student_user, created = User.objects.get_or_create(
                username=child_data['username'],
                defaults={
                    'first_name': child_data.get('first_name', ''),
                    'last_name': child_data.get('last_name', '')
                }
            )
            
            if created:
                student_user.set_password(child_data['password'])
                student_user.save()
                print("Created Student User:", student_user.username)
            else:
                print("User already exists:", student_user.username)
                
            try:
                class_instance = Class.objects.get(id=child_data['class_id'])
            except Class.DoesNotExist:
                return Response({"error": "Class not found"}, status=status.HTTP_400_BAD_REQUEST)    

          
            student = Student.objects.create(
                user=student_user,
                parent=parent,
                age=child_data['age'],
                class_id=class_instance,
                gender=child_data['gender'],
                username=child_data['username'],
                first_name=child_data.get('first_name', ''),  
                last_name=child_data.get('last_name', '')     
            )
            class_info = {
                "id": student.class_id.id,
                "class_name": student.class_id.class_name,
                "academic_year_start": student.class_id.academic_year_start,
                "academic_year_end": student.class_id.academic_year_end,
                "grade": student.class_id.grade
            }

            # Append detailed student information
            students.append({
                "first_name": student.user.first_name,
                "last_name": student.user.last_name,
                "age": student.age,
                "class_id": class_info,  # Include detailed class information
                "gender": student.gender,
                "username": student.user.username
            })

            # Build the response
            response_data = {
                "user": {
                    "username": parent_user.username,
                    "first_name": parent_user.first_name,
                    "last_name": parent_user.last_name,
                    "email": parent_user.email,
                    "password": parent_data['password']  # Avoid returning passwords in production
                },
                "address": address,
                "phone_number": phone_number,
                "gender": gender,
                "children": students  # Include the detailed students list
            }

        return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def parent_student_info(request):
    if request.user.is_authenticated:
        students = Student.objects.filter(parent__user=request.user)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)    
    return Response({'detail': 'Not authenticated'}, status=401)