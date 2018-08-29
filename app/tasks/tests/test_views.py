import pytest

from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory

from ..views import TaskViewSet

factory = APIRequestFactory()

pytestmark = pytest.mark.django_db

class TestTaskViews(object):
    def test_get_task_list(self):
        request = factory.get('/tasks/')
        resp = TaskViewSet.as_view({'get':'list'})(request)
        assert resp.status_code == 200, 'Status OK'

    def test_get_task_data(self):
        mixer.cycle().blend('tasks.TaskStatus', code=(x for x in range(5)))
        mixer.cycle().blend('tasks.Task', task_status=mixer.SELECT,
                reporter=None, assignee=None, parent=None)
        request = factory.get('/tasks/')
        resp = TaskViewSet.as_view({'get':'list'})(request)
        assert resp.render() and resp.serialize() != '', 'Serialize Data'
