# payments/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from chapa import Chapa
from .models import Payment
from .serializers import PaymentSerializer
import uuid


class PaymentInitializeView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def post(self, request):
        amount = request.data.get('amount')
        chapa = Chapa(settings.CHAPA_SECRET_KEY)
        tx_ref = str(uuid.uuid4())
        print(request.user.first_name)
        result = chapa.initialize(
            amount=amount,
            tx_ref=tx_ref,
            callback_url='http://localhost:8000/payments/payment/callback/',
            return_url='http://localhost:8000/payments/payment/callback/',
            first_name=request.user.first_name,
            last_name=request.user.last_name,
            email=request.user.email,
        )

        if result['status'] == 'success':
            payment = Payment.objects.create(
                user=request.user,
                chapa_tx_ref=tx_ref,
                amount=amount,
                status='pending'
            )
            return Response({
                'checkout_url': result['data']['checkout_url']
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Payment initialization failed'
        }, status=status.HTTP_400_BAD_REQUEST)


class PaymentCallbackView(generics.GenericAPIView):
    def get(self, request):
        tx_ref = request.GET.get('tx_ref')
        chapa = Chapa(settings.CHAPA_SECRET_KEY)
        result = chapa.verify(tx_ref)

        try:
            payment = Payment.objects.get(chapa_tx_ref=tx_ref)
            if result['status'] == 'success':
                payment.status = 'completed'
            else:
                payment.status = 'failed'
            payment.save()
            return Response({
                'status': payment.status,
                'message': result['message']
            }, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({
                'error': 'Payment not found'
            }, status=status.HTTP_404_NOT_FOUND)