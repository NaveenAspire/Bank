from django.http.response import JsonResponse
from bankapp.account import Account
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Benificiary, Employee_Profile, Customer_Profile
from .serializers import BenificiarySerializer, EmployeeSerializer, NewUserSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
import json


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer_Profile.objects.all()
    serializer_class = NewUserSerializer

    def create(self, request, *args, **kwargs):
        customer_detail = request.data

        new_customer = Customer_Profile.objects.create(
            user_name=customer_detail["user_name"],
            account_number=Account.account_number(),
            father_name=customer_detail["father_name"],
            email=customer_detail["email"],
            mobile=customer_detail["mobile"],
            dob=customer_detail["dob"],
            balance=0,
            password=customer_detail["password"],
        )

        new_customer.save()

        serializer = NewUserSerializer(new_customer)

        return Response(serializer.data)


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee_Profile.objects.all()
    serializer_class = EmployeeSerializer


class BenificiaryViewset(viewsets.ModelViewSet):
    queryset = Benificiary.objects.all()
    serializer_class = BenificiarySerializer


@api_view(["POST"])
def transfer(request):
    try:
        request = json.loads(request.body)
        amount = int(request.get("amount"))
        customer_acc = request.get("customer_acc")
        receiver_acc = request.get("receiver_acc")
        user = Customer_Profile.objects.get(account_number=customer_acc)
        receiver = Customer_Profile.objects.get(account_number=receiver_acc)

        if amount < user.balance:
            user.balance = user.balance - amount
            receiver.balance = receiver.balance + amount
            user.save()
            receiver.save()
            return JsonResponse("Amount Transfered Sucessfully", safe=False)
        else:
            return JsonResponse("Balance not available", safe=False)

    except:
        return JsonResponse("Post the valid detatils", safe=False)
