from django.db import router
from django.urls import path
from django.urls.conf import include
from .import views
from .apiViews import CustomerViewset, EmployeeViewset, BenificiaryViewset
from rest_framework import routers

from bankapp import apiViews

router = routers.DefaultRouter()
router.register('customer',CustomerViewset)
router.register('employee',EmployeeViewset)
router.register('benificiary',BenificiaryViewset)

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('customer/',views.customer,name='customer'),
    path('customer/password_reset',views.password_reset,name='password_reset'),
    path('customer/customer_profile',views.customer_profile,name='customer_profile'),
    path('customer/transfer',views.transfer,name='transfer'),
    path('employee/',views.employee,name='employee'),
    path('employee/emp_profile',views.emp_profile,name='emp_profile'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('employee/view_customer',views.view_customer,name='view_customer'),
    path('employee/transaction',views.transaction,name='transaction'),
    path('customer/customer_update',views.customer_update,name='customer_update'),
    path('customer/add_benificiary',views.add_benificiary,name='add_benificiary'),
    path('customer/benificiary_edit',views.benificiary_edit,name='benificiary_edit'),
    path('customer/remove_benificary',views.remove_benificary,name='remove_benificary'),
    path('customer/logout',views.logout_view,name='logout'),
    path('api/',include(router.urls)),
    path('api/transfer/',apiViews.transfer),
    
]