from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse
from django.views.generic import DetailView
from Account.models import Teacher, Student
from .models import Course
from .forms import CourseCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status, viewsets
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'Learning/course/list.html', {'courses': courses})


def payment(request, pk):
    if request.method == 'POST':
        transaction_id = str(request.POST.get('transaction_id'))

        if transaction_id.lower().startswith("eth"):

            return redirect(reverse('learning:enroll', kwargs={'pk': pk}))
        else:

            return HttpResponse('Invalid Transaction')
    return render(request, 'learning/pay/check.html', {'pk': pk})


@login_required
def enroll(request, pk):
    course = Course.objects.get(pk=pk)
    user = request.user
    username = user.username
    if user.is_student:
        user = Student.objects.get(username=username)
        user.enrolled_courses.add(course)
        response_content = f'Registered for a course  successfully'
        return redirect(reverse('learning:attend', kwargs={'pk': pk}))
    else:
        response_content = f'you can not enroll for a course by a teacher account'
        return HttpResponse(response_content)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'Learning/course/detail.html'
    context_object_name = 'course'


@login_required
def create_course(request):
    if request.user.is_anonymous:
        redirect('account:login')

    user = request.user
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

    return render(request, 'Learning/course/create.html', {'form': form, 'user': user})


def attend(request, pk):
    course = get_object_or_404(Course, pk=pk)
    sections = course.sections.all()

    return render(request, 'Learning/course/learn.html',
                  {'course': course, 'sections': sections})
