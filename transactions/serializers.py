from rest_framework import serializers
from .models import Payment, Invoice
from students.serializers import StudentSerializer 

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('date',)

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

# Combined serializer for Payment + Invoice response
class PaymentWithInvoiceSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'