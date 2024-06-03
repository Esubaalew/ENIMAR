from rest_framework import serializers
from .models import Course, Question, Quiz, Section, Choice, Subsection, File, Reading, CourseVideo, CoursePhoto


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class SubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = '__all__'


class CoursePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePhoto
        fields = '__all__'


class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = '__all__'
