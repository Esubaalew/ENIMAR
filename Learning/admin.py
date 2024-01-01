from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'created', 'updated']
    search_fields = ['title', 'teacher__firstname', 'teacher__lastname', 'description']
    list_filter = ['teacher__first_name', 'updated', 'created']
