from django.conf.urls import url

from .views import (
    MenuListAPIView,
    MenuCreateAPIView,
    MenuUpdateAPIView,
    MenuDetailAPIView,
    MenuDeleteAPIView,
)

urlpatterns = [
    url(r'^menu/list/$', MenuListAPIView.as_view(), name='menu-list'),
    url(r'^menu/create/$', MenuCreateAPIView.as_view(), name='menu-create'),
    url(r'^menu/(?P<pk>\d+)/update/$', MenuUpdateAPIView.as_view(), name='menu-update'),
    url(r'^menu/(?P<pk>\d+)/$', MenuDetailAPIView.as_view(), name='menu-detail'),
    url(r'^menu/(?P<pk>\d+)/delete/$', MenuDeleteAPIView.as_view(), name='menu-delete'),
]
