from rest_framework import serializers
from .models import Items, Tag
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Items.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'items', 'owner')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']


class ItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Items
        fields = ('id', 'title', 'price', 'image',
                  'tags', 'description', 'created_at', 'owner')


class CreateItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = ('id', 'title', 'price', 'image',
                  'tags', 'description', 'owner')
