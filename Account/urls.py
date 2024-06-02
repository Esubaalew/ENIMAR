from django.urls import path, include
from rest_framework import routers
from .views import UserSignInView, TeacherSignUp, StudentSignUp, UserViewSet, StudentViewSet, TeacherViewSet, \
    GetUserByUsername, UserPostListView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'teachers', TeacherViewSet, basename='teachers')

urlpatterns = [

    path('signup/teacher/', TeacherSignUp.as_view(), name='teacher-signup'),
    path('signup/student/', StudentSignUp.as_view(), name='student-signup'),
    path('signin/', UserSignInView.as_view(), name='user-signin'),
    path('user/<str:username>/', GetUserByUsername.as_view(), name='get-user-by-username'),
    path('user/<str:username>/posts/', UserPostListView.as_view(), name='user-resources'),
    path('', include(router.urls)),
]
