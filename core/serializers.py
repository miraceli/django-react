from dataclasses import fields
from .models import List, Item
from rest_framework import serializers

# como eu quero ver a api

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'done']

class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ['name', 'owner','url', 'item_set']

