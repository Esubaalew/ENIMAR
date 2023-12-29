from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Student, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_student', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_student', 'is_staff', 'is_active', 'groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'bio', 'position', 'address')}),
        (_('Permissions'), {'fields': ('is_student', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'updated')}),
    )
    readonly_fields = ('date_joined', 'last_login', 'updated')
    ordering = ('username',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_full_name', 'is_user_active', 'get_date_joined')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_filter = ('user__is_active', 'user__is_staff', 'user__groups', 'user__user_permissions')

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    def get_date_joined(self, obj):
        return obj.user.date_joined

    def is_user_active(self, obj):
        return obj.user.is_active

    get_full_name.short_description = _('Full Name')
    get_date_joined.short_description = _('Date Joined')
    is_user_active.short_description = _('User Active')
    get_full_name.admin_order_field = 'user__last_name'
    get_date_joined.admin_order_field = 'user__date_joined'
    is_user_active.admin_order_field = 'user__is_active'
