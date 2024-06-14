from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from rest_framework.decorators import action
from rest_framework.response import Response

from Account.models import CustomUser
from Account.serializers import UserSerializer
from .forms import PostCreationForm, CommentForm
from .models import Post, Comment, Photo, Video, Message, Share, Like
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import redirect, reverse
from rest_framework import generics, permissions, status, viewsets
from .serializers import PostSerializer, CommentSerializer, MessageSerializer, ShareSerializer, PhotoSerializer, \
    VideoSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        slug = slugify(title)
        serializer.save(author=self.request.user, slug=slug)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def likes(self, request, pk=None):
        post = self.get_object()
        likes = Like.objects.filter(post=post)
        serializer = LikeSerializer(likes, many=True)

        return Response(serializer.data)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
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
