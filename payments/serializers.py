from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'course', 'chapa_tx_ref', 'amount', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'course', 'chapa_tx_ref', 'status', 'created_at', 'updated_at']
