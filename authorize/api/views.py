from rest_framework import views, response, status

from authorize.models import Menu

from .serializers import MenuOutwardSerializer


class MenuListAPIView(views.APIView):

    @staticmethod
    def get(request):

        menus = Menu.objects.all()

        serializer = MenuOutwardSerializer(menus, many=True, fields=('id', 'name'))

        return response.Response(serializer.data, status=status.HTTP_200_OK)
