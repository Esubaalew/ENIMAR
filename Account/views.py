from rest_framework.views import APIView
from Learning.serializers import CourseSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView

from payments.models import Payment
from .models import CustomUser, Teacher, Student, Follow
from Learning.models import Course
from Social.models import Post, Comment, Photo, Video
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserSignInSerializer, StudentSerializer, TeacherSerializer, \
    StudentViewSerializer, TeacherViewSerializer, FollowSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, action, permission_classes
from Social.serializers import PostSerializer


# Update signup views to return user data
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
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
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
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignInView(generics.CreateAPIView):
    serializer_class = UserSignInSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
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

    @action(detail=True, methods=['get'])
    def followers(self, request, pk=None):
        user = self.get_object()
        followers = user.followers.all()
        serializer = FollowSerializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def following(self, request, pk=None):
        user = self.get_object()
        following = user.following.all()
        serializer = FollowSerializer(following, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        posts = user.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GetUserByUsername(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, username):
        try:
            user = CustomUser.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UserPostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(CustomUser, username=username)
        return Post.objects.filter(author=user)


class TeacherCourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs.get('username')
        teacher = get_object_or_404(Teacher, username=username)
        return Course.objects.filter(teacher=teacher)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def logged_in_user(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_teacher': user.is_teacher,

    }
    return Response(user_data)


class CoursesEnrolledByUserView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)

            payments = Payment.objects.filter(user=user).select_related('course')
            courses = [payment.course for payment in payments if payment.course]
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)