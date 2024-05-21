from django.urls import path,include
from rest_framework import routers
from . import views
from Social.views import PostViewSet,CommentViewSet,MessageViewSet,ShareViewSet,PhotoViewSet,VideoViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'shares', ShareViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('message/<int:recipient_id>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:other_user_id>/', views.conversation, name='conversation'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('share_post/<int:pk>/', views.share_post, name='share_post'),
    path('', include(router.urls)),

]
