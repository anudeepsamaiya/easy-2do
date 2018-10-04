from rest_framework import viewsets, filters
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter()
    serializer_class = TaskSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
            filters.OrderingFilter,)
    filterset_fields = ('title', 'description', 'parent')
    search_fields = ('ref_id', 'title', 'parent')
    ordering_fields = ('due_date', 'created')
