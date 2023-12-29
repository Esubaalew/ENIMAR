# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student


class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'second_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'bio',
            'position',
            'address')


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'second_name', 'username', 'email', 'password1', 'password2', 'phone_number'
        )

    def save(self, commit=True):
        user = super(StudentRegistrationForm, self).save(commit=False)

        # Set user as a student
        user.is_student = True
        if commit:
            user.save()

            # Create a Student instance associated with the user
            student = Student(user=user)
            student.save()

        return user
