from django.urls import path

from . import views
from .views import CustomLoginView

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
    path('logout/', views.logout_, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
]
