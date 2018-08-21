from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from tasks.views import *

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, base_name='task')

urlpatterns = router.urls

urlpatterns += []
