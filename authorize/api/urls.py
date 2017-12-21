from django.conf.urls import url

from .views import (
    MenuListAPIView
)

urlpatterns = [
    url(r'^menu/list/$', MenuListAPIView.as_view(), name='menu_list'),
]
