from django.urls import path, include
from rest_framework import routers
from .views import (
    CourseViewSet, QuizViewSet,
    QuestionViewSet, ChoiceViewSet,
    SectionViewSet, SubSectionViewSet,
    ReadingViewSet, FileViewSet,
    CourseVideoViewSet,
    CoursePhotoViewSet
)

app_name = 'learning'

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'quizzes', QuizViewSet, basename='quizzes')
router.register(r'questions', QuestionViewSet, 'questions')
router.register(r'choices', ChoiceViewSet, 'choices')
router.register(r'sections', SectionViewSet, 'sections')
router.register(r'sub-sections', SubSectionViewSet, 'sub-sections')
router.register(r'readings', ReadingViewSet, 'readings')
router.register(r'files', FileViewSet, 'files')
router.register(r'course-photos', CoursePhotoViewSet, 'course-photos')
router.register(r'course-videos', CourseVideoViewSet, 'course-videos')

urlpatterns = [
    path('', include(router.urls)),

]
