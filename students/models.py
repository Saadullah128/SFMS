from django.db import models

# Create your models here.

class Student(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    fee_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name