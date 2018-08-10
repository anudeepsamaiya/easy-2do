
from rest_framework import serializers
from .models import Category, SubCategory


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
    sub_categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'code']

    def validate_name(self, name):
        return name and name.title()

    def validate_code(self, code):
        return code and code.upper()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class SubCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
            allow_null=True)

    class Meta:
        model = SubCategory
        fields = []

    def validate_name(self, name):
        return name and name.title()

    def validate_code(self, code):
        return code and code.upper()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance

    def create(self, validated_data):
        return SubCategory.objects.create(**validated_data)
