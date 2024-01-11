from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/create', views.create_post, name='create_post')
]
