from django.urls import path,include
from . import views
from rest_framework import routers
from .views import CourseDetailView,CourseViewSet
app_name = 'learning'

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('courses/list', views.course_list, name='course_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('courses/enroll/<int:pk>', views.enroll, name='enroll'),
    path('payment/check/<int:pk>', views.payment, name='check'),
    path('course/attend/<int:pk>', views.attend, name='attend'),
    path('', include(router.urls)),
    
]
