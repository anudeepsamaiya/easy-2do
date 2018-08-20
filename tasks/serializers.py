
from rest_framework import serializers
from .models import Task, TaskStatus


class TaskSerializer(serializers.Serializer):
    ref_id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    task_status = serializers.PrimaryKeyRelatedField(queryset=TaskStatus.objects.all())
    parent = serializers.PrimaryKeyRelatedField(
            queryset=Task.objects.filter(parent__isnull=True), allow_null=True)

    class Meta:
        model = Task
        fields = []

    def update(self, instance, validated_data):
        instance.save()
        return instance

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
