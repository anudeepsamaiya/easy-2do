
from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = []
