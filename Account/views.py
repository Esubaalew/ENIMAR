from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser, Teacher, Student, Follow
from Learning.models import Course
from Social.models import Post, Comment, Photo, Video


def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    posts = Post.objects.all()

    context = {
        'courses': courses,
        'teachers': teachers,
        'students': students,
        'posts': posts,
    }
    if request.user.is_authenticated:
        return render(request, 'home.html', context=context)
    return render(request, 'guest.html', {'courses': courses})


class CustomLoginView(LoginView):
    template_name = 'Account/student/login.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_users'] = CustomUser.objects.all()
        return context

    def get_success_url(self):
        user = self.request.user

        if user.is_staff:
            return reverse('admin:index')
        else:
            return reverse('home')


@login_required
def logout_(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request, username):
    student = None
    teacher = None
    user = CustomUser.objects.get(username=username)
    if user.is_student:
        student = Student.objects.get(username=username)
    elif user.is_teacher:
        teacher = Teacher.objects.get(username=username)

    context = {'user': user, 'student': student, 'teacher': teacher}

    return render(request, 'Account/student/profile.html', context=context)


def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/account/login/')
    else:
        form = StudentRegistrationForm()

    return render(
        request,
        'Account/student/register.html',
        {'form': form})


def teacher_registration(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/account/login/')
    else:
        form = TeacherRegistrationForm()

    return render(
        request,
        'Account/teacher/register.html',
        {'form': form})


@login_required
def follow(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)

    if user_to_follow == request.user:
        redirect('account:profile', username=username)

    if not Follow.objects.filter(follower=request.user, followed=user_to_follow).exists():
        Follow.objects.create(follower=request.user, followed=user_to_follow)

    return redirect('account:profile', username=username)


@login_required
def unfollow(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)

    if user_to_unfollow == request.user:
        redirect('account:profile', username=username)

    Follow.objects.filter(follower=request.user, followed=user_to_unfollow).delete()
    return redirect('account:profile', username=username)
