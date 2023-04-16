from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Plant, Organization
from .serializer import *
from rest_framework.parsers import JSONParser
# Create your views here.

class plant_info(APIView):

    def get(self, request):
        plant_data = Plant.objects.all()
        serializer = PlantSerializers(plant_data, many=True)
        return Response(serializer.data)
    def post(self, request):
        # plant_data = JSONParser().parse(request)
        plant_data = request.data
        print(plant_data)
        print("data")
        plant_serializer = PlantSerializers(data=plant_data)
        if plant_serializer.is_valid():
            plant_serializer.save()
            return JsonResponse(plant_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(plant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)