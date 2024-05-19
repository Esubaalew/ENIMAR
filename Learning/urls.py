from django.urls import path,include
from . import views
from rest_framework import routers
from .views import CourseDetailView,CourseViewSet,QuizViewSet,QuestionViewSet,ChoiceViewSet,SectionViewSet,SubSectionViewSet,ReadingViewSet,FileViewSet,CourseVideoViewSet,CoursePhotoViewSet
app_name = 'learning'

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'sub-sections', SubSectionViewSet)
router.register(r'readings', ReadingViewSet)
router.register(r'files', FileViewSet)
router.register(r'course-photos', CoursePhotoViewSet)
router.register(r'course-videos', CourseVideoViewSet)

urlpatterns = [
    path('courses/list', views.course_list, name='course_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('courses/enroll/<int:pk>', views.enroll, name='enroll'),
    path('payment/check/<int:pk>', views.payment, name='check'),
    path('course/attend/<int:pk>', views.attend, name='attend'),
    path('', include(router.urls)),
    
]
