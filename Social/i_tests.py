# social/tests.py

"""
This file contains the test cases for the Social app integration testing.
It tests the API endpoints for posts, comments, messages, shares, photos, and videos.
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Account.models import CustomUser
from Learning.models import Course
from .models import Post, Comment, Message, Share, Photo, Video
from django.core.files.uploadedfile import SimpleUploadedFile
from Account.models import Teacher
class SocialIntegrationTest(APITestCase):
    def setUp(self):
        
        self.user1 = Teacher.objects.create(username='user1', password='pass1')
        self.user2 = CustomUser.objects.create(username='user2', password='pass2')
        
       
        self.course = Course.objects.create(
            title='Test Course', 
            description='Test description', 
            price=100.0,
            teacher=self.user1,
            poster=SimpleUploadedFile(name='test1.jpg', content=b'', content_type='image/jpeg')
        )

        
        self.photo = Photo.objects.create(image=SimpleUploadedFile(name='test2.jpg', content=b'', content_type='image/jpeg'))
        self.video = Video.objects.create(video_file=SimpleUploadedFile(name='test.mp4', content=b'', content_type='video/mp4'))
        
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            text='This is a test post',
            course=self.course,
            author=self.user1,
            video=self.video
        )
        self.post.photos.add(self.photo)
        
        # Create test comment
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user2,
            text='This is a test comment'
        )
        
        # Create test message
        self.message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            content='This is a test message'
        )
        
        # Create test share
        self.share = Share.objects.create(
            post=self.post,
            shared_by=self.user2
        )

    def test_post_list(self):
        url = reverse('posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_detail(self):
        url = reverse('posts-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_list(self):
        url = reverse('comments-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_detail(self):
        url = reverse('comments-detail', kwargs={'pk': self.comment.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_list(self):
        url = reverse('messages-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_message_detail(self):
        url = reverse('messages-detail', kwargs={'pk': self.message.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_share_list(self):
        url = reverse('shares-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_share_detail(self):
        url = reverse('shares-detail', kwargs={'pk': self.share.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_photo_list(self):
        url = reverse('photos-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_photo_detail(self):
        url = reverse('photos-detail', kwargs={'pk': self.photo.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_video_list(self):
        url = reverse('videos-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_video_detail(self):
        url = reverse('videos-detail', kwargs={'pk': self.video.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
