from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = router.urls

urlpatterns += []
