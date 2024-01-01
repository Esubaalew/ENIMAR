from django.urls import path

from . import views
from .views import CustomLoginView, CustomLogoutView

app_name = 'account'

urlpatterns = [path(
    'student-registration/',
    views.student_registration,
    name='student_registration'),
    path(
        'teacher-registration/',
        views.teacher_registration,
        name='teacher_registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('student/profile/', views.profile, name='profile')
]
