import pytest

from django.contrib.auth import get_user_model

from mixer.backend.django import mixer
from ..models import Task, TaskStatus

pytestmark = pytest.mark.django_db

class TestTask(object):

    def test_task_status(self):
        task_statuses = [Task.STATUS_DONE, Task.STATUS_IN_PROGRESS, Task.STATUS_PENDING]
        task_status_codes = (x for x in task_statuses)
        task_status = mixer.cycle(len(task_statuses)).blend(TaskStatus, code=task_status_codes)
        assert TaskStatus.objects.count() == len(task_statuses)

    def test_task_model(self):
        task_statuses = [Task.STATUS_DONE, Task.STATUS_IN_PROGRESS, Task.STATUS_PENDING]
        task_status_codes = (x for x in task_statuses)
        mixer.cycle(len(task_statuses)).blend(TaskStatus, code=task_status_codes)
        mixer.cycle(2).blend(get_user_model())
        obj = mixer.blend(Task,
                task_status=mixer.SELECT,
                reporter=mixer.SELECT, assignee=mixer.SELECT, parent=None,
            )
        assert obj.pk == 1, 'Should create a Task instance.'

    def test_subtask_model(self):
        task_statuses = [Task.STATUS_DONE, Task.STATUS_IN_PROGRESS, Task.STATUS_PENDING]
        task_status_codes = (x for x in task_statuses)
        mixer.cycle(len(task_statuses)).blend(TaskStatus, code=task_status_codes)
        task = mixer.blend(Task,
                task_status=mixer.SELECT,
                reporter=None, assignee=None, parent=None,
            )
        obj = mixer.blend(Task,
                task_status=mixer.SELECT,
                reporter=None, assignee=None, parent=None,
            )
        obj.parent = task
        obj.save()
        msg = 'Should create a SubTask instance. with a unique parent task'
        assert Task.objects.filter(ref_id=obj.parent_id).count() == 1, msg
