from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from users.models import Order
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
        wiggets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),
            "password1": forms.PasswordInput(attrs={'class': "form-control"}),
            "password2": forms.PasswordInput(attrs={'class': "form-control"}),
        }

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets={
            "mobile":forms.TextInput(attrs={'class': "form-control",'readonly':True}),
            "user": forms.HiddenInput(),
            "quantity":forms.NumberInput(attrs={'class': "form-control"}),
            "address":forms.Textarea(attrs={'class':"form-control",'required': True}),
            "status":forms.HiddenInput(),

        }
    def clean(self):
        cleaned_data=super().clean()
        quantity= cleaned_data.get('quantity')
        if quantity<1:
            msg = "Enter quantity greater than or equal to 1"
            self.add_error('quantity', msg)





class EditUserDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),


        }
