from django.urls import path
from . import views
from .views import CourseDetailView

app_name = 'learning'

urlpatterns = [
    path('courses/list', views.course_list, name='course_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('courses/enroll/<int:pk>', views.enroll, name='enroll'),
    path('payment/check/<int:pk>', views.payment, name='check'),
    
]
