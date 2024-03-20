from django.db import models
from Learning.models import Course
from Account.models import CustomUser


class Photo(models.Model):
    image = models.ImageField(upload_to='social/post/photos/')


class Video(models.Model):
    video_file = models.FileField(upload_to='social/post/videos/')


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    video = models.OneToOneField(Video, on_delete=models.CASCADE, null=True, blank=True)
    photos = models.ManyToManyField(Photo, related_name='posts', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='commenter')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)