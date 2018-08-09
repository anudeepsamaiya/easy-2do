from django.db import models
from usermanagement.models import User

class TaskStatus(models.Model):
    code = models.IntegerField()
    name = models.CharField(unique=True, max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TaskStatus'
        verbose_name = 'TaskStatus'
        verbose_name_plural = 'TaskStatuses'


class Tasks(models.Model):
    STATUS_TODO = 0
    STATUS_IN_PROGRESS = 1
    STATUS_DONE = 2

    reference_id = models.CharField(unique=True, max_length=13)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=250, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
            related_name='reported_tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
            related_name='assigned_tasks')
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_DEFAULT,
            default=0)

    def __str__(self):
        return ' '.join([self.reference_id, self.name])

    class Meta:
        db_table = 'Task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
