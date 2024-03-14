from django import forms

from Account.models import Teacher, Student
from .models import Post, Video, Course, Photo, Comment


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'course']

    video_file = forms.FileField(label='Upload Video', required=False)
    image_files = forms.FileField(
        label='Upload Photos', required=False, widget=forms.ClearableFileInput
    )

    def __init__(self, user, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        self.user = user
        user_name = user.username
        if user.is_teacher:
            teacher = Teacher.objects.get(username=user_name)
            self.fields['course'].queryset = Course.objects.filter(teacher=teacher)
        else:
            self.fields['video_file'].widget = forms.HiddenInput()
            self.fields['course'].widget = forms.HiddenInput()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
