from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Address

class AddressSerializer (ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class OpenAISerializer (serializers.Serializer):
    response = serializers.CharField()
    