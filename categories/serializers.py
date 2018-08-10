
from rest_framework import serializers
from .models import Category, SubCategory


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()

    class Meta:
        model = Category
        fields = ['name', 'code']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class SubCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()

    class Meta:
        model = SubCategory
        fields = []
