from django.urls import path,include
from rest_framework import routers
from .views import  UserSignInView,TeacherSignUp, StudentSignUp, UserViewSet,StudentViewSet,TeacherViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    
    path('signup/teacher/', TeacherSignUp.as_view(), name='teacher-signup'),
    path('signup/student/', StudentSignUp.as_view(), name='student-signup'),
    path('signin/', UserSignInView.as_view(), name='user-signin'),
    path('', include(router.urls)),
]
