from django.contrib import admin
from .models import Course, Assessment, Question, Choice, QuestionChoice

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
    model = Assessment
    extra = 1

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description')
    inlines = [QuestionInline]

class CourseAdmin(admin.ModelAdmin):
     list_display = ['title', 'teacher', 'created', 'updated']
     search_fields = ['title', 'teacher__firstname', 'teacher__lastname', 'description']
     list_filter = ['teacher__first_name', 'updated', 'created']
     inlines = [AssessmentInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'assessment')
    inlines = [QuestionChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text',)

class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice', 'is_correct')

admin.site.register(Course, CourseAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)


