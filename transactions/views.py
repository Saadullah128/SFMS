from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db import transaction
from .models import Payment, Invoice
from students.models import Student
from .serializers import PaymentWithInvoiceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentWithInvoiceSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        student_id = data.get('student')
        
        try:
            amount = Decimal(str(data.get('amount', 0)))  # Convert to Decimal
            student = Student.objects.get(id=student_id)
            
            if amount > student.fee_due:
                raise ValidationError({"error": "Payment exceeds outstanding balance!"})

            with transaction.atomic():
                payment = Payment.objects.create(
                    student=student,
                    amount=amount,
                    method=data.get('method'),
                    remarks=data.get('remarks', '')
                )
                Invoice.objects.create(payment=payment)
                student.fee_due -= amount  # Now both are Decimal
                student.save()

            serializer = self.get_serializer(payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)