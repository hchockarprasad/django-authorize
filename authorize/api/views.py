from rest_framework import views, response, status

from authorize.models import Menu

from .serializers import MenuOutwardSerializer, MenuCreateSerializer, MenuUpdateSerializer


# Endpoint to list menus with filters
class MenuListAPIView(views.APIView):

    @staticmethod
    def get(request):

        menus = Menu.objects.all()

        serializer = MenuOutwardSerializer(menus, many=True, fields=('id', 'name'))

        return response.Response(serializer.data, status=status.HTTP_200_OK)


# Endpoint to create new menu
class MenuCreateAPIView(views.APIView):

    @staticmethod
    def post(request):

        serializer = MenuCreateSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(status=status.HTTP_400_BAD_REQUEST)


# Endpoint to update an existing menu
class MenuUpdateAPIView(views.APIView):

    @staticmethod
    def put(request, pk):

        serializer = MenuUpdateSerializer(Menu.objects.get(pk=pk), data=request.data)

        if serializer.is_valid():

            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(status=status.HTTP_400_BAD_REQUEST)


# Endpoint to display menu details
class MenuDetailAPIView(views.APIView):

    @staticmethod
    def get(request, pk):

        menu = Menu.objects.get(pk=pk)

        serializer = MenuOutwardSerializer(menu, many=False)

        return response.Response(serializer.data, status=status.HTTP_200_OK)


# Endpoint to delete menu
class MenuDeleteAPIView(views.APIView):

    @staticmethod
    def delete(request, pk):

        menu = Menu.objects.get(pk=pk)

        menu.delete()

        return response.Response(status=status.HTTP_200_OK)
