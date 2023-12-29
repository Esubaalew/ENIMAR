from django.urls import path

from . import views
app_name = 'account'

urlpatterns = [path(
    'student-registration/',
    views.student_registration,
    name='student_registration'),
]
