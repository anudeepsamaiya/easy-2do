import pytest

from rest_framework.test import APIRequestFactory

from ..views import TaskViewSet

factory = APIRequestFactory()

pytestmark = pytest.mark.django_db

class TestTaskViews(object):
    def test_get_task_list(self):
        request = factory.get('/tasks/')
        resp = TaskViewSet.as_view({'get':'list'})(request)
        assert resp.status_code == 200, 'Status OK'
