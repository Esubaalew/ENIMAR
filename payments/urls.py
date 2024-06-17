from django.urls import path
from .views import PaymentInitializeView, PaymentCallbackView, PaymentsByTeacherView

app_name = 'payments'
urlpatterns = [
    path('initialize/', PaymentInitializeView.as_view(), name='api_payment_initialize'),
    path('callback/', PaymentCallbackView.as_view(), name='payment_callback'),
    path('teacher/<int:teacher_id>/', PaymentsByTeacherView.as_view(), name='payments-by-teacher'),
]
