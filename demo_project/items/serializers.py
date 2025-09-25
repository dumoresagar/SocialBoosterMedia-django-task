from rest_framework import serializers
from .models import Item, ExternalPost

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ExternalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalPost
        fields = "__all__"
