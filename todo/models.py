from django.db import models
from rest_framework import serializers


class Item(models.Model):

    class Status(models.TextChoices):
        TODO = 'todo'
        IN_PROGRESS = 'in_progress'
        DONE = 'done'

    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    status = models.CharField(choices=Status.choices, max_length=100, default=Status.TODO)
