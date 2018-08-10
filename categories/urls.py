
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name='category')
router.register(r'sub-categories', SubCategoryViewSet, base_name='sub-category')

urlpatterns = router.urls

urlpatterns += []
