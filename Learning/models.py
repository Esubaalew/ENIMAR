from django.contrib.auth.models import User
from django.db import models
from Account.models import Teacher, Student, CustomUser
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    poster = models.ImageField(upload_to='learning/course/posters/', help_text='An image representing the course')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='courses')
    students = models.ManyToManyField(Student, related_name='enrolled_courses', blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def has_content(self):
        return self.sections.exists() and any(section.subsections.exists() for section in self.sections.all())


class Quiz(models.Model):
    subsection = models.ForeignKey(
        'Subsection',
        on_delete=models.CASCADE,
        related_name='quizzes', default=None)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
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


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.name


class Subsection(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subsections')

    def __str__(self):
        return self.name


class Reading(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='readings', default=None)

    def __str__(self):
        return self.title


class File(models.Model):
    file_name = models.CharField(max_length=40)
    file_url = models.FileField(upload_to='learning/files')
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='files', default=None)

    def __str__(self):
        return self.file_name


class CoursePhoto(models.Model):
    image = models.ImageField(upload_to='learning/course/photos/')
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='photos', default=None)


class CourseVideo(models.Model):
    video_file = models.FileField(upload_to='learning/course/videos/')
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='videos', default=None)


class SubsectionCompletion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subsection_completions')
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='completions')
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'subsection']

    def __str__(self):
        return f'{self.user.username} completed {self.subsection.name}'
