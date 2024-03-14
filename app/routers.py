from django.db import models
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import DeviceS7View, ApiModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', DeviceS7View)

urlpatterns = [
    path('/data', include(router.urls)),
    path('/clp', ApiModelViewSet.as_view({'get': 'list'})),
]