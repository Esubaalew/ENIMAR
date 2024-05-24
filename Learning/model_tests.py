#model_test.py
'''
This file contains the tests for the models in the Learning app.

The tests will check if the models are created correctly and if the attributes are assigned correctly.

'''

from django.test import TestCase
from .models import Course, Section, Subsection
from Account.models import Teacher

class CourseModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create_user(
            username='teacheruser',
            password='teacherpass123',
            first_name='Teacher',
            last_name='User',
            is_teacher=True
        )
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course.',
            price=50.00,
            teacher=self.teacher
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, 'Test Course')
        self.assertEqual(self.course.description, 'This is a test course.')
        self.assertEqual(float(self.course.price), 50.00)
        self.assertEqual(self.course.teacher, self.teacher)

class SectionModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create_user(
            username='teacheruser',
            password='teacherpass123',
            first_name='Teacher',
            last_name='User',
            is_teacher=True
        )
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course.',
            price=50.00,
            teacher=self.teacher
        )
        self.section = Section.objects.create(
            name='Test Section',
            description='This is a test section.',
            course=self.course
        )

    def test_section_creation(self):
        self.assertEqual(self.section.name, 'Test Section')
        self.assertEqual(self.section.description, 'This is a test section.')
        self.assertEqual(self.section.course, self.course)

class SubsectionModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create_user(
            username='teacheruser',
            password='teacherpass123',
            first_name='Teacher',
            last_name='User',
            is_teacher=True
        )
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course.',
            price=50.00,
            teacher=self.teacher
        )
        self.section = Section.objects.create(
            name='Test Section',
            description='This is a test section.',
            course=self.course
        )
        self.subsection = Subsection.objects.create(
            name='Test Subsection',
            content='This is a test subsection.',
            section=self.section
        )

    def test_subsection_creation(self):
        self.assertEqual(self.subsection.name, 'Test Subsection')
        self.assertEqual(self.subsection.content, 'This is a test subsection.')
        self.assertEqual(self.subsection.section, self.section)
