from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from Account.models import CustomUser
from .forms import PostCreationForm, CommentForm
from .models import Post, Comment, Photo, Video, Message, Share
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import redirect, reverse
from rest_framework import generics, permissions, status, viewsets
from .serializers import PostSerializer, CommentSerializer, MessageSerializer, ShareSerializer, PhotoSerializer, \
    VideoSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        slug = slugify(title)
        serializer.save(author=self.request.user, slug=slug)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
