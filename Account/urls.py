from django.urls import path, include
from rest_framework import routers
from .views import UserSignInView, TeacherSignUp, StudentSignUp, UserViewSet, StudentViewSet, TeacherViewSet, \
    GetUserByUsername, UserPostListView, logged_in_user, TeacherCourseListView, CoursesEnrolledByUserView, \
    AccountantViewSet, PasswordResetRequestAPIView, PasswordResetConfirmAPIView, NotificationViewSet, \
    UserNotificationListView, FollowViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'accountants', AccountantViewSet, basename='accountants')
router.register(r'address', UserViewSet, basename='address')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'follows', FollowViewSet, basename='follows')

urlpatterns = [

    path('signup/teacher/', TeacherSignUp.as_view(), name='teacher-signup'),
    path('signup/student/', StudentSignUp.as_view(), name='student-signup'),
    path('signin/', UserSignInView.as_view(), name='user-signin'),
    path('user/<str:username>/', GetUserByUsername.as_view(), name='get-user-by-username'),
    path('user/<str:username>/posts/', UserPostListView.as_view(), name='user-posts'),
    path('teacher/<str:username>/courses/', TeacherCourseListView.as_view(), name='teacher-course-list'),
    path('loggedin/', logged_in_user, name='logged-in-user'),
    path('student/<int:user_id>/courses/', CoursesEnrolledByUserView.as_view(), name='courses-enrolled-by-user'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmAPIView.as_view(),
         name='password_reset_confirm'),
    path('user/<int:user_id>/notifications/', UserNotificationListView.as_view(), name='user_notifications'),
    path('', include(router.urls)),
]
