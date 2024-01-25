# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student, Teacher


class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user
