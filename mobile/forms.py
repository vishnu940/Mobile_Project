from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Product,Order,cart

class register_form(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]


class login_form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))


class product_create_form(ModelForm):
    class Meta:
        model=Product
        fields="__all__"

        widgets={
            "product_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "specs":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }

class order_form(ModelForm):
    class Meta:
        model=Order
        fields=["address","product","user"]

class cart_form(ModelForm):
    class Meta:
        model=cart
        fields="__all__"

        widgets={
            "product":forms.Select(attrs={"class":"form-control"}),
            "qty":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"})

        }






