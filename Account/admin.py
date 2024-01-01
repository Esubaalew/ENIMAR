from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Student, Address, Teacher


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country')
    list_filter = ('street', 'city', 'country', 'state')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_active', 'groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'bio', 'position', 'address')}),
        (_('Permissions'), {'fields': ('is_student', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'updated')}),
    )
    readonly_fields = ('date_joined', 'last_login', 'updated')
    ordering = ('username',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', ]
    search_fields = ('username', 'first_name', 'last_name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number', ]
    search_fields = ('username', 'first_name', 'last_name',)
