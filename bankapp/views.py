"""This module has django views"""
from django.contrib import messages
from django.db.transaction import (
    atomic,
    savepoint,
    savepoint_commit,
    savepoint_rollback,
)
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from bankapp.models import Benificiary, Customer_Profile, Employee_Profile
from bankapp.account import Account

# Create your views here.

def home(request):
    """This is home view for app"""

    return render(request, "home.html")

def about(request):
    """This is about view for app"""

    return render(request, "about.html")

def customer_register(request):
    """This is customer registration page view"""

    if request.method != "POST":
        return render(request, "customer_register.html")
    customer_name = request.POST.get("name")
    account_number = Account.account_number()
    father_name = request.POST.get("father_name")
    email = request.POST.get("email")
    mobile = request.POST.get("mobile")
    dob = request.POST.get("date_of_birth")
    balance = 0
    password = request.POST.get("psw")
    confirm_password = request.POST.get("psw-confirm")
    print(password, confirm_password)
    if password != confirm_password:
        messages.info(request, "Password And Confirm Password Not Same")
        return render(request, "customer_register.html")
    user = User.objects.create(username=email)
    user.password = make_password(password)
    Customer_Profile(
        customer_id=user.id,
        customer_name=customer_name,
        account_number=account_number,
        father_name=father_name,
        email=email,
        mobile=mobile,
        dob=dob,
        balance=balance,
    ).save()
    groups = Group.objects.get(name="Customer")
    groups.user_set.add(user)
    groups.save()
    user.save()
    return render(request, "customer.html")

def customer_login(request):
    """This is customer login view"""

    print("Test")
    if request.user.is_authenticated:
        return redirect("customer_profile")
    if request.method != "POST":
        return render(request, "customer.html")
    try:
        user = auth.authenticate(
            username=request.POST.get("email"), password=request.POST.get("psw")
        )
        if user is not None:
            auth.login(request, user)
            return redirect("customer_profile")
        messages.info(request, "Username or Password Invalid..")
        return redirect("customer_login")
    except Exception as e:
        pass

def password_reset(request):
    """This is password reset view for customer"""

    if request.method != "POST":
        return render(request, "password_reset.html")
    try:
        user = User.objects.get(username=request.POST.get("username"))
        customer = Customer_Profile.objects.get(customer_id=user.id)
        if customer.account_number != request.POST["account_number"]:
            messages.info(request, "Account Number not valid!")
            return redirect("password_reset")
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        if new_password != confirm_password:
            messages.info(request, "Password does not match!")
            return redirect("password_reset")
        user.password = make_password(new_password)
        user.save()
        messages.info(request, "Passwaord Changed!")
        return redirect("customer_login")
    except:
        messages.info(request, "Username does not exist!")
        return render(request, "password_reset.html")

@login_required(login_url="customer_login")
def customer_profile(request):
    """This is customer profile view"""

    try:
        print("So sad")
        customer = Customer_Profile.objects.get(customer_id=request.user.id)
        benificiary = Benificiary.objects.all().filter(
            customer_account=customer.account_number
        )
        context = {"benificiary": benificiary, "customer": customer}
        return render(request, "customer_profile.html", context)
    except:
        auth.logout(request)
        return redirect("customer_login")

def employee(request):
    """This is employee login view"""

    if request.method != "POST":
        return render(request, "employee.html")
    print(request.POST.get("psw"))
    print(request.POST.get("email"))
    user = auth.authenticate(
        username=request.POST.get("email"), password=request.POST.get("psw")
    )
    if user is None:
        messages.info(request, "Username or Password Invalid..")
        return redirect("emp_profile")
    auth.login(request, user)
    print(request.user.groups.all()[0])
    return redirect("emp_profile")

@login_required(login_url="employee")
def emp_profile(request):
    """This is employee profile view"""

    try:
        emp = Employee_Profile.objects.get(employee_id=request.user.id)
        return render(request, "emp_profile.html", {"employee": emp})
    except Exception as e:
        messages.info(request, "Username or Password Invalid..")
        auth.logout(request)
        return redirect("employee")

@login_required(login_url="customer_login")
@atomic
def transfer(request):
    """This is transaction view for customer"""

    if request.method != "POST":
        return redirect("customer_profile")
    reciever_acc = request.POST["reciever_acc"]
    amount = int(request.POST["amount"])
    if Customer_Profile.objects.filter(account_number=reciever_acc).exists():
        customer = Customer_Profile.objects.get(customer_id=request.user.id)
        if customer.balance >= amount:
            reciever = Customer_Profile.objects.get(account_number=reciever_acc)
            customer.balance = customer.balance - amount
            rid = savepoint()
            customer.save()
            try:
                # raise ValueError
                reciever.balance = reciever.balance + amount
                reciever.save()
                savepoint_commit(rid)
                return redirect("customer_profile")
            except Exception as e:
                savepoint_rollback(rid)
                return redirect("customer_profile")
        else:
            messages.info(request, "Insufficient Balance..", extra_tags="transfer")
    else:
        messages.info(request, "Account Number Not Exist..", extra_tags="transfer")
        return redirect("customer_profile")

@login_required(login_url="customer_login")
def customer_update(request):
    """This is customer profile update view"""

    customer = Customer_Profile.objects.get(customer_id=request.user.id)
    if request.method != "POST":
        return render(request, "customer_update.html")
    customer_name = request.POST.get("name")
    father_name = request.POST.get("father_name")
    mobile = request.POST.get("mobile")
    dob = request.POST.get("date_of_birth")
    customer.customer_name = customer_name
    customer.father_name = father_name
    customer.mobile = mobile
    customer.dob = dob
    customer.save()
    return redirect("customer_profile")

@login_required(login_url="employee")
def view_customer(request):
    """This is view customers by employee view"""

    if request.method != "POST":
        return redirect("emp_profile")
        
    account_number = request.POST["account_num"]
    if Customer_Profile.objects.filter(account_number=account_number).exists():
        request.session["account_number"] = account_number
        customer = Customer_Profile.objects.get(account_number=account_number)
        emp = Employee_Profile.objects.get(employee_id=request.user.id)
        context = {"customer": customer, "employee": emp}
        return render(request, "emp_profile.html", context)
    else:
        if "account_number" in request.session:
            del request.session["account_number"]
        messages.info(request, "Account Number Not Exist")
        return redirect("emp_profile")

@login_required(login_url="employee")
def transaction(request):
    """This is transaction view for employee"""

    if request.method != "POST":
        return redirect("emp_profile")
    account_number = request.POST["account_num"]
    amount = int(request.POST.get("amount"))
    if Customer_Profile.objects.filter(account_number=account_number).exists():
        customer = Customer_Profile.objects.get(account_number=account_number)
        if request.POST["action"] == "withdraw":
            if customer.balance >= amount:
                customer.balance = customer.balance - amount
                customer.save()
                redirect("emp_profile")
        else:
            if amount > 0:
                customer.balance = customer.balance + amount
                customer.save()
                return redirect("emp_profile")
    return redirect("emp_profile")

@login_required(login_url="customer_login")
def add_benificiary(request):
    """This is add benificiary account by customer view"""

    if request.method != "POST":
        return redirect("customer_profile")
    customer = Customer_Profile.objects.get(customer_id=request.user.id)
    customer_account = customer.account_number
    holder_name = request.POST["benificiary_name"]
    holder_nickname = request.POST["benificiary_nickname"]
    account_number = request.POST["benificiary_acc"]
    if Customer_Profile.objects.filter(account_number=account_number).exists():
        Benificiary(
            customer_account=customer_account,
            name=holder_name,
            nick_name=holder_nickname,
            account_number=account_number,
        ).save()
        return redirect("customer_profile")
    else:
        messages.info(request, "Account Number Not exist..", extra_tags="benificiary")
        return redirect("customer_profile")

@login_required(login_url="customer_login")
def benificiary_edit(request):
    """This view used for manage the benificiary accounts by customer"""

    customer = Customer_Profile.objects.get(customer_id=request.user.id)
    benificiary = Benificiary.objects.all().filter(
        customer_account=customer.account_number
    )
    context = {"benificiary": benificiary, "customer": customer}
    return render(request, "benificiary_edit.html", {"context": context})

@login_required(login_url="customer_login")
def remove_benificary(request):
    """This vies used for remove the benificiary by customer"""

    if request.method != "POST":
        return redirect("benificiary_edit")
    Benificiary.objects.filter(account_number=request.POST["action"]).delete()
    return redirect("benificiary_edit")

def logout_view(request):
    """This view used for logout customer"""

    auth.logout(request)
    request.session.flush()
    return redirect("/")
