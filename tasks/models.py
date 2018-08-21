from django.db import models
from django_extensions.db import models as model_extensions
from usermanagement.models import User

class TaskStatus(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(unique=True, max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TaskStatus'
        verbose_name = 'TaskStatus'
        verbose_name_plural = 'TaskStatuses'


class AbstractTask(model_extensions.TitleSlugDescriptionModel,
        model_extensions.TimeStampedModel, model_extensions.ActivatorModel):

    STATUS_PENDING = 0
    STATUS_IN_PROGRESS = 1
    STATUS_DONE = 2

    ref_id = models.CharField(unique=True, max_length=13)
    task_status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)

    def __str__(self):
        return ' : '.join([self.ref_id, self.slug])

    class Meta:
        abstract = True


class Task(AbstractTask):
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
            related_name='reported_tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
            related_name='assigned_tasks')
    due_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'Task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
