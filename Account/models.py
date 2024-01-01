from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
    def __str__(self):
        parts = [self.street, self.city, self.state, self.country]

        address_parts = filter(None, parts)
        return ', '.join(address_parts)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True)
    position = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "All User"

    def __str__(self):
        return self.username


class Student(CustomUser):

    class Meta:
        verbose_name = "Student"


class Teacher(CustomUser):

    class Meta:
        verbose_name = "Teacher"
