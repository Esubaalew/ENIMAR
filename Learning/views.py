from Account.models import Teacher
from .models import Course, Quiz, Question, Choice, Section, Subsection, File, Reading, CoursePhoto, CourseVideo
from rest_framework import permissions, viewsets
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, SectionSerializer, ChoiceSerializer, \
    FileSerializer, ReadingSerializer, SubSectionSerializer, CoursePhotoSerializer, CourseVideoSerializer


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


class CourseVideoViewSet(viewsets.ModelViewSet):
    queryset = CourseVideo.objects.all()
    serializer_class = CourseVideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CoursePhotoViewSet(viewsets.ModelViewSet):
    queryset = CoursePhoto.objects.all()
    serializer_class = CoursePhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'Learning/course/list.html', {'courses': courses})


# def payment(request, pk):
#     if request.method == 'POST':
#         transaction_id = str(request.POST.get('transaction_id'))

#         if transaction_id.lower().startswith("eth"):

#             return redirect(reverse('learning:enroll', kwargs={'pk': pk}))
#         else:

#             return HttpResponse('Invalid Transaction')
#     return render(request, 'learning/pay/check.html', {'pk': pk})


# @login_required
# def enroll(request, pk):
#     course = Course.objects.get(pk=pk)
#     user = request.user
#     username = user.username
#     if user.is_student:
#         user = Student.objects.get(username=username)
#         user.enrolled_courses.add(course)
#         response_content = f'Registered for a course  successfully'
#         return redirect(reverse('learning:attend', kwargs={'pk': pk}))
#     else:
#         response_content = f'you can not enroll for a course by a teacher account'
#         return HttpResponse(response_content)


# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'Learning/course/detail.html'
#     context_object_name = 'course'


# @login_required
# def create_course(request):
#     if request.user.is_anonymous:
#         redirect('account:login')

#     user = request.user
#     if request.method == 'POST':
#         form = CourseCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             course = form.save(commit=False)

#             user = request.user
#             username = user.username
#             teacher = Teacher.objects.get(username=username)
#             course.teacher = teacher
#             course.save()
#             return redirect('learning:course_detail', pk=course.pk)
#     else:
#         form = CourseCreationForm()

#     return render(request, 'Learning/course/create.html', {'form': form, 'user': user})


# def attend(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     sections = course.sections.all()

#     return render(request, 'Learning/course/learn.html',
#                   {'course': course, 'sections': sections})
