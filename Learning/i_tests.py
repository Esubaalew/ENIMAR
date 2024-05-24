# learning/tests.py

"""This file contains the test cases for the Learning app integration testing. It tests the API endpoints for
courses, quizzes, questions, choices, sections, subsections, readings, files, course photos, and course videos.

"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Account.models import Teacher, CustomUser
from .models import Course, Quiz, Question, Choice, Section, Subsection, Reading, File, CoursePhoto, CourseVideo
from django.core.files.uploadedfile import SimpleUploadedFile


class CourseIntegrationTest(APITestCase):
    def setUp(self):
        self.teacher_user = CustomUser.objects.create(username='teacher', is_teacher=True)
        self.teacher = Teacher.objects.create(username='ttttttt')

        self.course = Course.objects.create(
            title='Test Course',
            description='Test description',
            price=100.0,
            teacher=self.teacher,
            poster=SimpleUploadedFile(name='test1.jpg', content=b'', content_type='image/jpeg')
        )
        self.section = Section.objects.create(name='Test Section', description='Test section description',
                                              course=self.course)
        self.subsection = Subsection.objects.create(name='Test Subsection', content='Test subsection content',
                                                    section=self.section)
        self.quiz = Quiz.objects.create(name='Test Quiz', description='Test quiz description',
                                        subsection=self.subsection)
        self.question = Question.objects.create(quiz=self.quiz, question_text='Test question')
        self.choice = Choice.objects.create(choice_text='Test choice', description='Test choice description')
        self.reading = Reading.objects.create(title='Test Reading', content='Test reading content',
                                              subsection=self.subsection)
        self.file = File.objects.create(file_name='Test File',
                                        file_url=SimpleUploadedFile(name='t.txt', content=b'Test file content',
                                                                    content_type='text/plain'),
                                        subsection=self.subsection)
        self.course_photo = CoursePhoto.objects.create(
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            subsection=self.subsection)
        self.course_video = CourseVideo.objects.create(
            video_file=SimpleUploadedFile(name='test.mp4', content=b'', content_type='video/mp4'),
            subsection=self.subsection)

    def test_course_list(self):
        url = reverse('learning:courses-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
