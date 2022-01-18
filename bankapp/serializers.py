from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Benificiary, Employee_Profile, Customer_Profile

class NewUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer_Profile
        fields = '__all__'
        read_only_fields = ("account_number","balance")


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee_Profile
        fields = '__all__'
        

class BenificiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Benificiary
        fields = '__all__'
        


