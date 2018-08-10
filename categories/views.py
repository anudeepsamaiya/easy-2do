
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('code', 'name',
            'sub_categories__name', 'sub_categories__code')


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('code', 'name', 'category__code', 'category__name')
