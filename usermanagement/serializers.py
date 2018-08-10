
from rest_framework import serializers
from usermanagement.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = []
