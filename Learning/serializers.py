from rest_framework import serializers
from .models import Course, Question, Quiz, Section, Choice, Subsection, File, Reading, CourseVideo, CoursePhoto, \
    SubsectionCompletion


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['teacher']

    def validate_published(self, value):
        if value:
            if self.instance and not self.instance.has_content():
                raise serializers.ValidationError(
                    "A course must have sections and non-empty subsections to be published.")
        return value


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


class SubsectionCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubsectionCompletion
        fields = '__all__'
        read_only_fields = ['user', 'subsection']
        extra_kwargs = {
            'completed': {'write_only': True}
        }
