from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Customer_Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=11)
    father_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    balance = models.IntegerField()

    def __str__(self):
        return self.account_number


class Employee_Profile(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=20)
    employee_email = models.EmailField()
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.employee_email


class Benificiary(models.Model):
    name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=11)
    customer_account = models.CharField(max_length=11)

    def __str__(self):
        return self.nick_name
