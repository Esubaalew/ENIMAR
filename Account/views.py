from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser, Teacher, Student, Follow
from Learning.models import Course
from Social.models import Post, Comment, Photo, Video
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserSignInSerializer,StudentSerializer,TeacherSerializer,StudentViewSerializer,TeacherViewSerializer
from rest_framework.permissions import AllowAny

class StudentSignUp(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherSignUp(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSignInView(generics.CreateAPIView):
    serializer_class = UserSignInSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# def home(request):
#     courses = Course.objects.all()
#     teachers = Teacher.objects.all()
#     students = Student.objects.all()
#     posts = Post.objects.all()

#     context = {
#         'courses': courses,
#         'teachers': teachers,
#         'students': students,
#         'posts': posts,
#     }
#     if request.user.is_authenticated:
#         return render(request, 'home.html', context=context)
#     return render(request, 'guest.html', {'courses': courses})



# @login_required
# def logout_(request):
#     logout(request)
#     return redirect('home')


# @login_required
# def profile(request, username):
#     student = None
#     teacher = None
#     user = CustomUser.objects.get(username=username)
#     if user.is_student:
#         student = Student.objects.get(username=username)
#     elif user.is_teacher:
#         teacher = Teacher.objects.get(username=username)

#     context = {'user': user, 'student': student, 'teacher': teacher}

#     return render(request, 'Account/student/profile.html', context=context)


# def student_registration(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/account/login/')
#     else:
#         form = StudentRegistrationForm()

#     return render(
#         request,
#         'Account/student/register.html',
#         {'form': form})


# def teacher_registration(request):
#     if request.method == 'POST':
#         form = TeacherRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/account/login/')
#     else:
#         form = TeacherRegistrationForm()

#     return render(
#         request,
#         'Account/teacher/register.html',
#         {'form': form})


# @login_required
# def follow(request, username):
#     user_to_follow = get_object_or_404(CustomUser, username=username)

#     if user_to_follow == request.user:
#         redirect('account:profile', username=username)

#     if not Follow.objects.filter(follower=request.user, followed=user_to_follow).exists():
#         Follow.objects.create(follower=request.user, followed=user_to_follow)

#     return redirect('account:profile', username=username)


# @login_required
# def unfollow(request, username):
#     user_to_unfollow = get_object_or_404(CustomUser, username=username)

#     if user_to_unfollow == request.user:
#         redirect('account:profile', username=username)

#     Follow.objects.filter(follower=request.user, followed=user_to_unfollow).delete()
#     return redirect('account:profile', username=username)
