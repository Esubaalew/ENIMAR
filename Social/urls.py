from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('message/<int:recipient_id>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:other_user_id>/', views.conversation, name='conversation'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('share_post/<int:pk>/', views.share_post, name='share_post'),

]
