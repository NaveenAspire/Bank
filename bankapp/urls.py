"""This is module used for implementing the urls"""
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from bankapp import apiViews
from . import views
from .apiViews import CustomerViewset, EmployeeViewset, BenificiaryViewset


router = routers.DefaultRouter()
router.register("customer", CustomerViewset)
router.register("employee", EmployeeViewset)
router.register("benificiary", BenificiaryViewset)

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("customer_login/", views.customer_login, name="customer_login"),
    path("customer_login/password_reset", views.password_reset, name="password_reset"),
    path(
        "customer_login/customer_profile",
        views.customer_profile,
        name="customer_profile",
    ),
    path("customer_login/transfer", views.transfer, name="transfer"),
    path("employee/", views.employee, name="employee"),
    path("employee/emp_profile", views.emp_profile, name="emp_profile"),
    path("customer_register", views.customer_register, name="customer_register"),
    path("employee/view_customer", views.view_customer, name="view_customer"),
    path("employee/transaction", views.transaction, name="transaction"),
    path(
        "customer_login/customer_update", views.customer_update, name="customer_update"
    ),
    path(
        "customer_login/add_benificiary", views.add_benificiary, name="add_benificiary"
    ),
    path(
        "customer_login/benificiary_edit",
        views.benificiary_edit,
        name="benificiary_edit",
    ),
    path(
        "customer_login/remove_benificary",
        views.remove_benificary,
        name="remove_benificary",
    ),
    path("customer_login/logout", views.logout_view, name="logout"),
    path("api/", include(router.urls)),
    path("api/transfer/", apiViews.transfer),
]
