from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from Account.models import Teacher,Student
from .models import Course
from .forms import CourseCreationForm
from django.http import HttpResponse

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'Learning/course/list.html', {'courses': courses})
@login_required
def enroll(request,pk):
    course = Course.objects.get(pk=pk)
    user=request.user
    username=user.username
    if user.is_student:
       user=Student.objects.get(username=username)
       user.courses.add(course)
       response_content = f'Registered for a course  successfully'
       return HttpResponse(response_content)
    else:
        response_content = f'you can not enroll for a course by a teacher account'
        return HttpResponse(response_content)



class CourseDetailView(DetailView):
    model = Course
    template_name = 'Learning/course/detail.html'
    context_object_name = 'course'


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)

            user = request.user
            username = user.username
            teacher = Teacher.objects.get(username=username)
            course.teacher = teacher
            course.save()
            return redirect('learning:course_detail', pk=course.pk)
    else:
        form = CourseCreationForm()

    return render(request, 'Learning/course/create.html', {'form': form, })
