from django.urls import path
from .views import PaymentInitializeView, PaymentCallbackView

app_name = 'payments'
urlpatterns = [
    path('payment/', PaymentInitializeView.as_view(), name='api_payment_initialize'),
    path('payment/callback/', PaymentCallbackView.as_view(), name='api_payment_callback'),
]
