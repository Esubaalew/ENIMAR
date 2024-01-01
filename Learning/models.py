from django.contrib.auth.models import User
from django.db import models
from django.db.models import ManyToManyField
from Account.models import Teacher, Student
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    poster = models.ImageField(upload_to='Learning/course/posters/', help_text='An image representing the course')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student, related_name='courses', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})