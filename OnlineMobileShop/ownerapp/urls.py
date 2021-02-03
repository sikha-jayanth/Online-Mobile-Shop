"""OnlineMobileShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ownerapp.views import *

urlpatterns = [
    path("create",createBrand,name="createbrand"),
    path("deletebrand<int:pk>",deleteBrand,name="deletebrand"),
    path("updatebrand<int:pk>",updateBrand,name="updatebrand"),
    path("createmobile",createMobile,name="createmobile"),
    path("ownerhome",listMobile,name="listmobile"),
    path("viewmobile<int:pk>",viewMobile,name="viewmobile"),
    path("deletemobile<int:pk>",deleteMobile,name="deletemobile"),
    path("updatemobile<int:pk>",updateMobile,name="updatemobile"),
    path("viewuserorders",viewUserOrders,name="userorders"),
    path("userorderdetails<int:pk>",viewUserOrderDetails,name="userorderdetails"),
]
