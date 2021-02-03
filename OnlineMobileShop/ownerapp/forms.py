from django import forms
from django.forms import ModelForm
from ownerapp.models import Mobile,Brand
from users.models import Order
class BrandCreateForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={'class':"form-control"}),
        }
    def clean(self):
        cleaned_data=super().clean()
        brandname=cleaned_data.get("brand_name")
        brand=Brand.objects.filter(brand_name=brandname)
        if(brand):
            msg="Brand name already exists"
            self.add_error('brand_name',msg)

class BrandUpdateForm(ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {
            "brand_name": forms.TextInput(attrs={'class': "form-control"}),
        }
    def clean(self):
        cleaned_data=super().clean()
        brandname=cleaned_data.get("brand_name")
        brand=Brand.objects.filter(brand_name=brandname)
        if(brand):
            msg="Brand name already exists"
            self.add_error('brand_name',msg)


class mobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
        "mobile_name":forms.TextInput(attrs={'class':"form-control"}),
        "Mobile_brand":forms.Select(attrs={'class':"form-control"}),
        "ram":forms.TextInput(attrs={'class':"form-control"}),
        "internal_storage":forms.TextInput(attrs={'class':"form-control"}),
        "color":forms.TextInput(attrs={'class':"form-control"}),
        "screen_size":forms.TextInput(attrs={'class':"form-control"}),
        "processor":forms.TextInput(attrs={'class':"form-control"}),
        "price":forms.TextInput(attrs={'class':"form-control"}),
        "image":forms.FileInput(attrs={'class':"form-control"}),
        }

    def clean(self):
        cleaned_data=super().clean()
        mobilename=cleaned_data.get('mobile_name')
        price=cleaned_data.get('price')
        mobile=Mobile.objects.filter(mobile_name=mobilename)
        if mobile:
            msg = "Mobile already exists"
            self.add_error('mobile_name', msg)
        if price < 1500:
            msg = "Enter price greater than 1500"
            self.add_error('price', msg)




class OwnerOrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets={
            "mobile":forms.TextInput(attrs={'class': "form-control",'readonly':True}),
            "user": forms.TextInput(attrs={'class': "form-control",'readonly':True}),
            "quantity":forms.NumberInput(attrs={'class': "form-control",'readonly':True}),
            "address":forms.Textarea(attrs={'class':"form-control",'readonly':True}),
            "status":forms.Select(attrs={'class': "form-control"}),

        }


