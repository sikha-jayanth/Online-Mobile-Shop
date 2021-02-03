from django.shortcuts import render, redirect
from ownerapp.forms import BrandCreateForm,BrandUpdateForm,mobileCreationForm,OwnerOrderForm
from ownerapp.models import Brand,Mobile
from users.models import Order

# Create your views here.
def createBrand(request):
    form=BrandCreateForm()
    context={}
    context["form"]=form
    queryset = Brand.objects.all()
    context["brands"] = queryset
    if request.method=='POST':
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, "owner/brandcreation.html", context)
        else:
            context["form"]=form
            return render(request, "owner/brandcreation.html", context)


    return render(request, "owner/brandcreation.html", context)

def deleteBrand(request,pk):

    Brand.objects.get(id=pk).delete()
    return redirect("createbrand")


def updateBrand(request,pk):
    brand=Brand.objects.get(id=pk)
    form=BrandUpdateForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BrandUpdateForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createbrand")
    return render(request,"owner/brandupdate.html",context)

def createMobile(request):
    form=mobileCreationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=mobileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"]=form
            return render(request, "owner/createmobile.html", context)

    return render(request,"owner/createmobile.html",context)


def listMobile(request):
    context={}
    queryset=Mobile.objects.all()
    context["mobiles"]=queryset
    return render(request,"owner/listmobile.html",context)

def viewMobile(request,pk):
    context={}
    queryset=Mobile.objects.get(id=pk)
    context["mobile"]=queryset
    return render(request,"owner/viewmobile.html",context)

def deleteMobile(request,pk):
    Mobile.objects.get(id=pk).delete()
    return redirect("listmobile")

def updateMobile(request,pk):
    mobile=Mobile.objects.get(id=pk)
    form=mobileCreationForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=mobileCreationForm(instance=mobile,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"]=form
            return render(request, "owner/mobileupdate.html", context)
    return render(request,"owner/mobileupdate.html",context)



def viewUserOrders(request):
    context={}
    orders=Order.objects.all()
    context["orders"]=orders
    return render(request,"owner/vieworder.html",context)



def viewUserOrderDetails(request,pk):
    order=Order.objects.get(id=pk)
    form=OwnerOrderForm(instance=order)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=OwnerOrderForm(instance=order,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("userorders")
        else:
            context["form"]=form
            return render(request,"owner/userorderdetails.html",context)
    return render(request, "owner/userorderdetails.html", context)












