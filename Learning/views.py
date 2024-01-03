from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from Account.models import Teacher
from .models import Course
from .forms import CourseCreationForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'Learning/course/list.html', {'courses': courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'Learning/course/detail.html'
    context_object_name = 'course'


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)

            user = request.user
            username = user.username
            teacher = Teacher.objects.get(username=username)
            course.teacher = teacher
            course.save()
            return redirect('learning:course_detail', pk=course.pk)
    else:
        form = CourseCreationForm()

    return render(request, 'Learning/course/create.html', {'form': form, })
