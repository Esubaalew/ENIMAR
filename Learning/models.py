from django.contrib.auth.models import User
from django.db import models


from Account.models import Teacher, Student
from django.urls import reverse
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    poster = models.ImageField(upload_to='Learning/course/posters/', help_text='An image representing the course')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='courses')
    students = models.ManyToManyField(Student, related_name='enrolled_courses', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('learning:course_detail', args=[str(self.pk)])


class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assessments')
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)
    choices = models.ManyToManyField('Choice', through='QuestionChoice', related_name='questions')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.choice_text
    

class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choices')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='question_choices')
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.choice.choice_text
    
   