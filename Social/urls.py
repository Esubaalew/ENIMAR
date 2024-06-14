from django.urls import path, include
from rest_framework import routers
from Social.views import PostViewSet, CommentViewSet, MessageViewSet, ShareViewSet, PhotoViewSet, VideoViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'messages', MessageViewSet, basename='messages')
router.register(r'shares', ShareViewSet, basename='shares')
router.register(r'photos', PhotoViewSet, basename='photos')
router.register(r'videos', VideoViewSet, basename='videos')

urlpatterns = [
    path('', include(router.urls)),

]
