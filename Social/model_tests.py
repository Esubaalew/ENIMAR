from django.test import TestCase
from Learning.models import Course
from Account.models import CustomUser
from .models import Photo, Video, Post, Comment
from Account.models import Teacher
from django.core.exceptions import ValidationError

# Utility function to create a Post instance
def create_post(title="Test Post", author=None, course=None, text="", video=None, photos=[]):
    if not author:
        author = CustomUser.objects.create_user(username="testuser", password="test123")
    post = Post.objects.create(
        title=title, author=author, text=text, course=course, video=video
    )
    post.photos.set(photos)
    return post

class PostModelTest(TestCase):

    def test_create_post(self):
        """Tests successful creation of a Post instance."""
        post = create_post()
        self.assertIsInstance(post, Post) 
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.text, "")
        self.assertEqual(post.course, None)
        self.assertEqual(post.video, None)
        self.assertEqual(list(post.photos.all()), [])

    def test_create_post_with_course(self):
        """Tests creation of a Post with a linked Course."""
        course = Course.objects.create(title="Test Course", price=50.00, teacher=Teacher.objects.create_user(username="teacher", password="pass123"))
        post = create_post(course=course)
        self.assertEqual(post.course, course)

    def test_create_post_with_video(self):
        """Tests creation of a Post with a linked Video."""
        video = Video.objects.create(video_file="test.mp4") 
        post = create_post(video=video)
        self.assertEqual(post.video, video)

    def test_create_post_with_photos(self):
        """Tests creation of a Post with multiple Photos."""
        photos = Photo.objects.bulk_create([
            Photo(image="test1.jpg"),
            Photo(image="test2.jpg"),
        ])
        post = create_post(photos=photos)
        self.assertEqual(list(post.photos.all()), photos)

    def test_total_likes(self):
        """Tests the `total_likes` method."""
        post = create_post()
        user1 = CustomUser.objects.create_user(username="user1", password="pass123")
        user2 = CustomUser.objects.create_user(username="user2", password="pass456")
        post.likes.add(user1, user2)
        self.assertEqual(post.total_likes(), 2)

    def test_comment_creation(self):
        """Tests creation of a Comment associated with a Post."""
        post = create_post()
        user = CustomUser.objects.create_user(username="commenter", password="commentpass")
        comment = Comment.objects.create(post=post, user=user, text="This is a test comment.")
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.text, "This is a test comment.")

