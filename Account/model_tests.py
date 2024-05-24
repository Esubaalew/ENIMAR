# model_tests.py

"""
11 tests = passed

### AddressModelTest:
1. test_address_creation:
    - Purpose: Verifies that an Address instance is created successfully with the provided street, city, state, and country.
    - Expected Result: An Address instance should be created, and its string representation should match the expected format.
    - Test Result: Passed. The Address instance is successfully created, and its string representation matches the expected format.

2. test_address_without_street:
    - Purpose: Tests the behavior when creating an Address without providing a street.
    - Expected Result: The Address instance should still be created, and its string representation should omit the street.
    - Test Result: Passed. An Address instance is created without a street, and its string representation excludes the street.

3. test_address_without_state:
    - Purpose: Tests the behavior when creating an Address without providing a state.
    - Expected Result: The Address instance should still be created, and its string representation should omit the state.
    - Test Result: Passed. An Address instance is created without a state, and its string representation excludes the state.

### CustomUserModelTest:
1. test_user_creation:
    - Purpose: Verifies that a CustomUser instance is created successfully with the provided username, password, first name, last name, and phone number.
    - Expected Result: A CustomUser instance should be created, its string representation should match the username, and its full name should be correctly formatted.
    - Test Result: Passed. The CustomUser instance is successfully created, its string representation matches the username, and the full name is correctly formatted.

2. test_user_with_address:
    - Purpose: Tests the behavior when associating an Address with a CustomUser.
    - Expected Result: The CustomUser instance should be associated with the provided Address instance.
    - Test Result: Passed. The Address is associated with the CustomUser instance as expected.

### StudentModelTest & TeacherModelTest:
- These test cases follow a similar structure to CustomUserModelTest, ensuring that Student and Teacher instances are created successfully and their respective flags (is_student and is_teacher) are set correctly.

### FollowModelTest:
1. test_follow_creation:
    - Purpose: Verifies that a Follow instance is created successfully with the provided follower and followed users.
    - Expected Result: A Follow instance should be created, and its string representation should indicate the follower-followed relationship.
    - Test Result: Passed. The Follow instance is successfully created, and its string representation indicates the follower-followed relationship.

2. test_follow_unique_constraint:
    - Purpose: Tests the behavior when attempting to create a duplicate Follow instance (same follower-followed relationship).
    - Expected Result: Creating a duplicate Follow instance should raise a unique constraint error.
    - Test Result: Passed. An exception is raised as expected when attempting to create a duplicate Follow instance.

3. test_follower_deletion & test_followed_deletion:
    - Purpose: Verifies that when a follower or followed user is deleted, the corresponding Follow instances are also deleted.
    - Expected Result: Follow instances associated with the deleted user should be removed from the database.
    - Test Result: Passed. Follow instances associated with the deleted user are successfully deleted from the database.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Address, CustomUser, Student, Teacher, Follow

# Get the custom user model
User = get_user_model()


class AddressModelTest(TestCase):
    """Test cases for the Address model."""

    def setUp(self):
        """Set up an address instance for testing."""
        self.address = Address.objects.create(
            street='123 Main St',
            city='Anytown',
            state='Anystate',
            country='USA'
        )

    def test_address_creation(self):
        """Test if the address instance is created correctly."""
        self.assertTrue(isinstance(self.address, Address))
        self.assertEqual(self.address.__str__(), '123 Main St, Anytown, Anystate, USA')

    def test_address_without_street(self):
        """Test the address string representation when street is not provided."""
        address = Address.objects.create(
            city='Anytown',
            state='Anystate',
            country='USA'
        )
        self.assertEqual(address.__str__(), 'Anytown, Anystate, USA')

    def test_address_without_state(self):
        """Test the address string representation when state is not provided."""
        address = Address.objects.create(
            street='123 Main St',
            city='Anytown',
            country='USA'
        )
        self.assertEqual(address.__str__(), '123 Main St, Anytown, USA')


class CustomUserModelTest(TestCase):
    """Test cases for the CustomUser model."""

    def setUp(self):
        """Set up a custom user instance for testing."""
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User',
            phone_number='1234567890'
        )

    def test_user_creation(self):
        """Test if the custom user instance is created correctly."""
        self.assertTrue(isinstance(self.user, CustomUser))
        self.assertEqual(self.user.__str__(), 'testuser')
        self.assertEqual(self.user.get_full_name(), 'Test User')

    def test_user_with_address(self):
        """Test if the user can be linked to an address."""
        address = Address.objects.create(
            street='123 Main St',
            city='Anytown',
            state='Anystate',
            country='USA'
        )
        self.user.address = address
        self.user.save()
        self.assertEqual(self.user.address, address)


class StudentModelTest(TestCase):
    """Test cases for the Student model."""

    def setUp(self):
        """Set up a student user instance for testing."""
        self.student = Student.objects.create_user(
            username='studentuser',
            password='studentpass123',
            first_name='Student',
            last_name='User',
            is_student=True
        )

    def test_student_creation(self):
        """Test if the student user instance is created correctly."""
        self.assertTrue(isinstance(self.student, Student))
        self.assertTrue(self.student.is_student)


class TeacherModelTest(TestCase):
    """Test cases for the Teacher model."""

    def setUp(self):
        """Set up a teacher user instance for testing."""
        self.teacher = Teacher.objects.create_user(
            username='teacheruser',
            password='teacherpass123',
            first_name='Teacher',
            last_name='User',
            is_teacher=True
        )

    def test_teacher_creation(self):
        """Test if the teacher user instance is created correctly."""
        self.assertTrue(isinstance(self.teacher, Teacher))
        self.assertTrue(self.teacher.is_teacher)


class FollowModelTest(TestCase):
    """Test cases for the Follow model."""

    def setUp(self):
        """Set up two user instances and a follow instance for testing."""
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass1')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass2')
        self.follow = Follow.objects.create(follower=self.user1, followed=self.user2)

    def test_follow_creation(self):
        """Test if the follow instance is created correctly."""
        self.assertTrue(isinstance(self.follow, Follow))
        self.assertEqual(self.follow.__str__(), 'user1 follows user2')

    def test_follow_unique_constraint(self):
        """Test that creating a duplicate follow relationship raises an error."""
        with self.assertRaises(Exception):
            Follow.objects.create(follower=self.user1, followed=self.user2)  # Should raise a unique constraint error

    def test_follower_deletion(self):
        """Test that deleting the follower also deletes the follow relationship."""
        follow_exists_before_delete = Follow.objects.filter(follower=self.user1, followed=self.user2).exists()
        self.assertTrue(follow_exists_before_delete)
        self.user1.delete()
        follow_exists_after_delete = Follow.objects.filter(follower_id=self.user1.id,
                                                           followed_id=self.user2.id).exists()
        self.assertFalse(follow_exists_after_delete)

    def test_followed_deletion(self):
        """Test that deleting the followed user also deletes the follow relationship."""
        follow_exists_before_delete = Follow.objects.filter(follower=self.user1, followed=self.user2).exists()
        self.assertTrue(follow_exists_before_delete)
        self.user2.delete()
        follow_exists_after_delete = Follow.objects.filter(follower_id=self.user1.id,
                                                           followed_id=self.user2.id).exists()
        self.assertFalse(follow_exists_after_delete)
