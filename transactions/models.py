
# Create your models here.
from django.db import models
from students.models import Student  # Import Student model
from django.utils import timezone

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Online', 'Online'),
        ('Card', 'Card'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.student.name}"
    

class Invoice(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='invoice')
    invoice_number = models.CharField(max_length=20, unique=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    quickbooks_ref = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only for new invoices
            super().save(*args, **kwargs)  # Save first to get an ID
            year = timezone.now().year
            self.invoice_number = f"INV-{year}-{self.id:03d}"
            kwargs['force_insert'] = False  # Prevent duplicate save
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number   