from django.db.models import Q
from rest_framework import serializers
from Account.serializers import UserSerializer
from .models import Group, Message


class GroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'members']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'group', 'content', 'timestamp']


class LatestMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']


class PrivateChatSerializer(serializers.Serializer):
    user = UserSerializer()
    latest_message = LatestMessageSerializer()