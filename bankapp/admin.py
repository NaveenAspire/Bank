from bankapp.models import Benificiary, Customer_Profile, Employee_Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Customer_Profile)
admin.site.register(Employee_Profile)
admin.site.register(Benificiary)
