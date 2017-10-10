from django.db import models
from django.conf import settings
from datetime import date
from django.contrib import admin
# Create your models here.

class User(models.Model):

    ACTIVE = 'Active'
    PENDING = 'Pending'
    DORMANT = 'Dormant'
    BLOCKED = 'Blocked'
    STATUS = (
        (ACTIVE, 'Active'),
        (PENDING, 'Pending'),
        (DORMANT, 'Dormant'),
        (BLOCKED, 'Blocked'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(unique=True,max_length=8,default=12345678)
    phone_no = models.CharField(unique=True,max_length=12,default=254712345678)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=15,choices=STATUS,default=PENDING)
    loan_limit = models.FloatField(default=200.00)
    residence = models.CharField(max_length=100)
    device_id = models.BigIntegerField(unique=True,default=0)


class Loan(models.Model):

    ACTIVE  = 'Active'
    PENDING = 'Pending'
    DORMANT = 'Dormant'
    BLOCKED = 'Blocked'
    STATUS  = (
        (ACTIVE, 'Active'),
        (PENDING, 'Pending'),
        (DORMANT, 'Dormant'),
        (BLOCKED, 'Blocked'),
    )

    user = models.ForeignKey(
	    User,
	    on_delete=models.CASCADE,
	    verbose_name="Loan Applicant",
    )
    applicationDate = models.DateField()
    dueDate = models.DateField()
    loan_amount = models.FloatField(default=0.00)
    loan_balance = models.FloatField(default=0.00)
    status = models.CharField(max_length=15,choices=STATUS,default=PENDING)
   
  






	


