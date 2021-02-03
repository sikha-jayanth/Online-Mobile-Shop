from django.shortcuts import render,redirect
from users.forms import RegistrationForm,OrderForm,EditUserDetailsForm
from ownerapp.models import Mobile,Brand
from users.models import Order
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def userRegistration(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"]=form
            return render(request, "users/registration.html", context)

    return render(request,"users/registration.html",context)


def userLogin(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        user=authenticate(request,username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return redirect("userhome")
    return render(request,"users/login.html")

@login_required(login_url='login')
def userHome(request):
    context = {}
    queryset = Mobile.objects.all()
    context["mobiles"] = queryset
    return render(request, "users/userhome.html", context)

@login_required(login_url='login')
def orderMobile(request,pk):
    mobile=Mobile.objects.get(id=pk)
    mobilename=mobile.mobile_name
    form=OrderForm(initial={"mobile":mobilename,"user":request.user})
    context={}
    context["form"]=form
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vieworder")
        else:
            form=OrderForm(request.POST)
            context["form"]=form
            return render(request, "users/ordermobile.html", context)

    return render(request,"users/ordermobile.html",context)

@login_required(login_url='login')
def viewOrder(request):
    context={}
    orders=Order.objects.filter(user=request.user)
    context["orders"]=orders
    return render(request,"users/vieworder.html",context)

@login_required(login_url='login')
def cancelOrder(request,pk):
    Order.objects.get(id=pk).delete()
    return redirect("vieworder")

def viewOrderDetails(request,pk):
    context={}
    order=Order.objects.get(id=pk)
    context["order"]=order
    return render(request,"users/vieworderdetails.html",context)


@login_required(login_url='login')
def userLogout(request):
    logout(request)
    return redirect("login")

def editUserDetails(request):
    user=User.objects.get(username=request.user)
    form=EditUserDetailsForm(instance=user)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=EditUserDetailsForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("userhome")
        else:
            context["form"]=form
            return render(request,"users/editprofile.html",context)
    return render(request, "users/editprofile.html", context)

def viewMobileDetails(request,pk):
    context={}
    queryset=Mobile.objects.get(id=pk)
    context["mobile"]=queryset
    return render(request,"users/viewmobiledetails.html",context)


