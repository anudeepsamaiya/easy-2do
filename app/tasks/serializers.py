
from rest_framework import serializers
from .models import Task, TaskStatus


class TaskSerializer(serializers.Serializer):
    ref_id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    due_date = serializers.DateField()
    task_status = serializers.PrimaryKeyRelatedField(queryset=TaskStatus.objects.all())
    parent = serializers.PrimaryKeyRelatedField(
            queryset=Task.objects.filter(parent__isnull=True), allow_null=True)

    class Meta:
        model = Task
        fields = []

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.task_status = validated_data.get('task_status',
                instance.task_status)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()
        return instance

    def create(self, validated_data):
        return Task.objects.create(**validated_data)


class TaskStatusSerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()

    class Meta:
        model = TaskStatus
        fields = []

    def validate_name(self, name):
        return name and name.title()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance

    def create(self, validated_data):
        return TaskStatus.objects.create(**validated_data)
