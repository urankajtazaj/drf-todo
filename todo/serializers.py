from rest_framework import serializers
from todo.models import Item


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'status']
        partial = True
