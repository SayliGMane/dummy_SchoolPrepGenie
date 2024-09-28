from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.teacher.models.lunchmenu import LunchMenu
from apps.teacher.serializer.lunchmenu  import LunchMenuSerializer


@api_view(['GET', 'POST'])
def lunch_menu_view(request):
    if request.method == 'GET':
        menus = LunchMenu.objects.all()
        serializer = LunchMenuSerializer(menus, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LunchMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)