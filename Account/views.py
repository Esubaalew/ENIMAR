from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser, Teacher, Student
from Learning.models import Course


def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()

    return render(request, 'home.html', {'courses': courses, 'teachers': teachers, 'students': students})


class CustomLoginView(LoginView):
    template_name = 'Account/student/login.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_users'] = CustomUser.objects.all()
        return context

    def get_success_url(self):
        return '/home'


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
