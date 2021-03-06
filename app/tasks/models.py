from datetime import datetime
from random import randint

from django.db import models
from django_extensions.db import models as model_extensions

from commons.models import Alert
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
    def generate_task_ref_id(initial='task-', *args, **kwargs):
        ts = str(datetime.today().strftime('%Y%m%d:%H%M%S'))
        postfix = str(kwargs.get('postfix', '')) or str(randint(2,100))
        return initial + ts + postfix

    ref_id = models.CharField(unique=True, max_length=13,
            default=generate_task_ref_id)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
            related_name='reported_tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
            related_name='assigned_tasks')
    due_date = models.DateField(null=True)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE,
            related_name='subtask', to_field='ref_id', null=True,
            limit_choices_to={'parent__isnull':True},
        )

    class Meta:
        db_table = 'Task'


class TaskAlert(Alert):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
            related_name='alerts')

    class Meta:
        db_table = 'TaskAlert'
