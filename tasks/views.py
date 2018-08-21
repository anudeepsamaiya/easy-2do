from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskViewSet(viewsets.ViewSet):

    def list(self, *args, **kwargs):
        queryset = Task.objects.all()
        task_serializer = TaskSerializer(queryset, many=True)
        return Response(task_serializer.data)

