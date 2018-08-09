
from rest_framework import serializers
from .models import Category, SubCategory

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = []


class SubCategorySerializer(serializers.Serializer):
    class Meta:
        model = SubCategory
        fields = []
