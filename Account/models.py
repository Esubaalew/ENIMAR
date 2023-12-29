from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=10)

    def __str__(self):
        parts = [self.street, self.city, self.state, self.country]

        address_parts = filter(None, parts)
        return ', '.join(address_parts)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True)
    position = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True)

    def __str__(self):
        return self.user.username
