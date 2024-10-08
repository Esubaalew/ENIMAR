from django.contrib import admin
from .models import (
    Course,
    Quiz,
    Question,
    Choice,
    QuestionChoice,
    Reading,
    File,
    CoursePhoto,
    CourseVideo, Subsection, Section, SubsectionCompletion
)


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionChoiceInline(admin.TabularInline):
    model = QuestionChoice
    extra = 4


class AssessmentInline(admin.TabularInline):
    model = Quiz
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'subsection', 'description')
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'created', 'updated']
    search_fields = ['title', 'teacher__firstname', 'teacher__lastname', 'description']
    list_filter = ['teacher__first_name', 'updated', 'created']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz')
    inlines = [QuestionChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text',)


class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice', 'is_correct')


admin.site.register(Course, CourseAdmin)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'subsection')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseVideo)
class CourseVideoAdmin(admin.ModelAdmin):
    pass


@admin.register(CoursePhoto)
class CoursePhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')


@admin.register(SubsectionCompletion)
class SubsectionCompletionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subsection', 'completed_date')
