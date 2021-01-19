from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from datetime import datetime
from .serializers import ItemSerializer, UserSerializer, CreateItemSerializer
from django.contrib.auth.models import User
from .models import Items
from api.permissions import IsOwnerOrReadOnly
# Create your views here.


class Userlist(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateItemView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = CreateItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItemView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
