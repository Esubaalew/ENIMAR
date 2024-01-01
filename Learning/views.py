from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from Learning.models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'Learning/course/list.html', {'courses': courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'Learning/course/detail.html'
    context_object_name = 'course'
