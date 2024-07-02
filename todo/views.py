from django.shortcuts import render
from rest_framework import permissions, viewsets
from todo.models import Item
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
