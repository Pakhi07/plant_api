from rest_framework import serializers
from .models import Plant, Organization



class PlantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ("id", "SellerName", "name", "description", "price", "image", "available")

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("id", "name", "description", "number_people", "bioScore", "image")