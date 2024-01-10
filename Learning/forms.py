from django.forms import ModelForm
from Learning.models import Course

class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['teacher', 'students']

