from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from usermanagement.models import User
from usermanagement.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer()

    def create(self, *args, **kwargs):
        return super(UserViewSet, self).create(*args, **kwargs)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
