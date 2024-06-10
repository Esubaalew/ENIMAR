from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('course', 'amount', 'created_at', 'updated_at')
    list_filter = ('course', 'created_at', 'updated_at')
    search_fields = ('course', 'amount')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

