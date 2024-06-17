from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from chapa import Chapa
from Learning.models import Course
from .models import Payment
from .serializers import PaymentSerializer
import uuid
import requests


class PaymentInitializeView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def post(self, request):
        try:
            amount = request.data.get('amount')
            course_id = request.data.get('course')
            course = None
            if course_id:
                course = Course.objects.get(id=course_id)

            if course and Payment.objects.filter(user=request.user, course=course).exists():
                return Response({
                    'error': 'You have already made a payment for this course.'
                }, status=status.HTTP_400_BAD_REQUEST)

            chapa = Chapa(settings.CHAPA_SECRET_KEY)
            tx_ref = str(uuid.uuid4())
            result = chapa.initialize(
                amount=amount,
                tx_ref=tx_ref,
                callback_url='http://localhost:8000/payments/callback/?tx_ref=tx_ref',
                first_name=request.user.first_name,
                last_name=request.user.last_name,
                email=request.user.email,
            )

            if result['status'] == 'success':
                Payment.objects.create(
                    user=request.user,
                    course=course,
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
        except Course.DoesNotExist:
            return Response({
                'error': 'Course not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'error': 'An unexpected error occurred'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentCallbackView(generics.GenericAPIView):
    def get(self, request):
        tx_ref = request.GET.get('tx_ref')

        chapa_endpoint = settings.CHAPA_VERIFY_ENDPOINT
        chapa_secret_key = settings.CHAPA_SECRET_KEY

        headers = {
            "Authorization": f"Bearer {chapa_secret_key}"
        }
        response = requests.get(f"{chapa_endpoint}/{tx_ref}", headers=headers)
        result = response.json()

        try:
            payment = Payment.objects.get(chapa_tx_ref=tx_ref)

            if result['status'] == 'success':
                payment.status = 'completed'
            else:
                payment.status = 'failed'

            payment.save()

            payment_details = result.get('data', {})
            payer_details = {
                'first_name': payment_details.get('first_name'),
                'last_name': payment_details.get('last_name'),
                'email': payment_details.get('email'),
                'phone_number': payment_details.get('phone_number'),
                'currency': payment_details.get('currency'),
                'amount': payment_details.get('amount'),
                'charge': payment_details.get('charge'),
                'mode': payment_details.get('mode'),
                'method': payment_details.get('method'),
                'type': payment_details.get('type'),
                'status': payment_details.get('status'),
                'reference': payment_details.get('reference'),
                'tx_ref': payment_details.get('tx_ref'),
                'customization': payment_details.get('customization', {}),
                'meta': payment_details.get('meta', {}),
                'created_at': payment_details.get('created_at'),
                'updated_at': payment_details.get('updated_at')
            }

            return Response({
                'status': payment.status,
                'message': result.get('message', 'No message provided'),
                'payer_details': payer_details
            }, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({
                'error': 'Payment not found'
            }, status=status.HTTP_404_NOT_FOUND)


class PaymentsByTeacherView(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Payment.objects.filter(course__teacher__id=teacher_id)
