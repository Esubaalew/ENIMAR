from rest_framework.decorators import action
from rest_framework.response import Response
from Account.models import Teacher, CustomUser
from Account.serializers import UserSerializer
from payments.models import Payment
from .models import Course, Quiz, Question, Choice, Section, Subsection, File, Reading, CoursePhoto, CourseVideo, \
    SubsectionCompletion
from rest_framework import permissions, viewsets, generics, status
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, SectionSerializer, ChoiceSerializer, \
    FileSerializer, ReadingSerializer, SubSectionSerializer, CoursePhotoSerializer, CourseVideoSerializer, \
    SubsectionCompletionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_teacher:
            teacher_instance = Teacher.objects.get(id=self.request.user.id)
            serializer.save(teacher=teacher_instance)
        else:
            raise ValueError("Only teachers can create courses.")

    @action(detail=True, methods=['get'])
    def sections(self, request, pk=None):
        course = self.get_object()
        sections = Section.objects.filter(course=course)
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def subsections(self, request, pk=None):
        section = self.get_object()
        subsections = Subsection.objects.filter(section=section)
        serializer = SubSectionSerializer(subsections, many=True)
        return Response(serializer.data)


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubSectionViewSet(viewsets.ModelViewSet):
    queryset = Subsection.objects.all()
    serializer_class = SubSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def readings(self, request, pk=None):
        subsection = self.get_object()
        readings = subsection.readings.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def files(self, request, pk=None):
        subsection = self.get_object()
        files = subsection.files.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def photos(self, request, pk=None):
        subsection = self.get_object()
        photos = subsection.photos.all()
        serializer = CoursePhotoSerializer(photos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def videos(self, request, pk=None):
        subsection = self.get_object()
        videos = subsection.videos.all()
        serializer = CourseVideoSerializer(videos, many=True)
        return Response(serializer.data)


class CourseVideoViewSet(viewsets.ModelViewSet):
    queryset = CourseVideo.objects.all()
    serializer_class = CourseVideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoursePhotoViewSet(viewsets.ModelViewSet):
    queryset = CoursePhoto.objects.all()
    serializer_class = CoursePhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudentsWhoPaidForCourseView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']  # status = 'completed'
        payments = Payment.objects.filter(course_id=course_id)
        user_ids = payments.values_list('user_id', flat=True)
        return CustomUser.objects.filter(id__in=user_ids)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubsectionCompletionViewSet(viewsets.ModelViewSet):
    queryset = SubsectionCompletion.objects.all()
    serializer_class = SubsectionCompletionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)