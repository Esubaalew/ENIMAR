#i_tests.py 

"""
This file contains the test cases for the Account app integration testing.
It tests the API endpoints for student and teacher signup, and user signin.

The test_student_signup_success method tests the student signup API endpoint.
The test_teacher_signup_success method tests the teacher signup API endpoint.
The test_user_signin_success method tests the user signin API endpoint.

This  test insures that the API endpoints for student and teacher signup, and user signin are working correctly.
and also insures that different  components  of the app are working together correctly. 
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