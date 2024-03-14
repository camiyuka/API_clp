from django.shortcuts import render
from app.models import ApiModel
from rest_framework import viewsets
from .serializers import ApiModelSerializer
from django.http import JsonResponse

class ApiModelViewSet(viewsets.ViewSet):
    def list(self, request):
        api_models = ApiModel.objects.last()
        serializer= ApiModelSerializer(api_models, many= True)
        return render(request, 'api_model_view.html', {'api_models': serializer.data})

class DeviceS7View(viewsets.ModelViewSet):
    queryset = ApiModel.objects.all()
    serializer_class = ApiModelSerializer
