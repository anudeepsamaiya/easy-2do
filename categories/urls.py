
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name='category')

urlpatterns = router.urls

urlpatterns += []
