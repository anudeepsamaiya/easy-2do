
from rest_framework import serializers
from tasks.models import Tasks


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Tasks
        fields = []
