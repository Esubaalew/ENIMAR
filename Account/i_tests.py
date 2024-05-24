#i_tests.py 

"""
This file contains the test cases for the Account app integration testing.
It tests the API endpoints for student and teacher signup, user signin, and user-related actions.

Integration testing in Django Rest Framework refers to testing the interaction between different components of the
application, such as models, views, serializers, and URLs, to ensure they work together correctly.

The `test_student_signup_success` method tests the student signup API endpoint. It sends a POST request to the
'student-signup' URL with sample data and asserts that the response status code is 201 (HTTP_CREATED). It also
asserts that the username in the response data matches the username in  sent data and that the password field is
not present in the response data.

The `test_teacher_signup_success` method tests the teacher signup API endpoint. It sends a POST request to the
'teacher-signup' URL with sample data and asserts that the response status code is 201 (HTTP_CREATED). It also
asserts that the username in the response data matches the username in  sent data and that the password field is
not present in the response data.

The `test_user_signin_success` method tests the user signin API endpoint. It creates a test user using the CustomUser
model, sends a POST request to the 'user-signin' URL with the test user's credentials, and asserts that the response
status code is 200 (HTTP_OK). It also asserts that the response data contains 'refresh' and 'access' tokens.

The `UserViewSetTestCase` class contains test cases for user-related actions. The `test_followers` method tests the
'users-followers' URL, which retrieves the followers of a user. It sends a GET request to the URL with the user's
primary key (pk) as a parameter and asserts that the response status code is 200 (HTTP_OK).

The `test_following` method tests the 'users-following' URL, which retrieves the users that a user is following. It
sends a GET request to the URL with the user's primary key (pk) as a parameter and asserts that the response status
code is 200 (HTTP_OK).

The `test_posts` method tests the 'users-posts' URL, which retrieves the posts of a user. It sends a GET request to
the URL with the user's primary key (pk) as a parameter and asserts that the response status code is 200 (HTTP_OK).

The `StudentViewSetTestCase` class contains a test case for listing students.
The `test_list` method tests the 'students-list' URL, which retrieves a list of students.
It sends a GET request to the URL and asserts that the response status code is 200 (HTTP_OK).

The `TeacherViewSetTestCase` class contains a test case for listing teachers.
The `test_list` method tests the 'teachers-list' URL, which retrieves a list of teachers.
It sends a GET request to the URL and asserts that the response status code is 200 (HTTP_OK).
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser


class AccountAPITestCase(APITestCase):

    def test_student_signup_success(self):
        data = {'username': 'test_student', 'password': 'strong_password',
                'first_name': 'Test', 'last_name': 'Student'}
        response = self.client.post(reverse('student-signup'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['username'], data['username'])
        self.assertFalse('password' in response.data)

    def test_teacher_signup_success(self):
        data = {'username': 'test_teacher', 'password': 'strong_password',
                'first_name': 'Test', 'last_name': 'Teacher'}
        response = self.client.post(reverse('teacher-signup'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['username'], data['username'])
        self.assertFalse('password' in response.data)

    def test_user_signin_success(self):
        user = CustomUser.objects.create_user(username='test_user', password='correct_password')
        data = {'username': 'test_user', 'password': 'correct_password'}
        response = self.client.post(reverse('user-signin'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='user1', password='password1')
        self.user2 = CustomUser.objects.create_user(username='user2', password='password2')

    def test_followers(self):
        url = reverse('users-followers', kwargs={'pk': self.user1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_following(self):
        url = reverse('users-following', kwargs={'pk': self.user1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_posts(self):
        url = reverse('users-posts', kwargs={'pk': self.user1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StudentViewSetTestCase(APITestCase):
    def test_list(self):
        url = reverse('students-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeacherViewSetTestCase(APITestCase):
    def test_list(self):
        url = reverse('teachers-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
