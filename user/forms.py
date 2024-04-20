from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

# class C_login(forms.Form):
#     class Meta:
#         model = User
#         fields = ["username", "password"]

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'username',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
    }))


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}),
            'email': forms.EmailInput(
                attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}),
            'password': forms.PasswordInput(
                attrs={'class': 'rounded-0 my-0', 'style': 'border:none; border-bottom: 1px solid rgb(33, 37, 41)'}),
        }
        help_texts = {
            'username': 'Letters, digits and @/./+/-/_ only.',
        }

    # def is_valid_email(self):
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     a = re.match(pattern, self.cleaned_data['email'])
    #     if a != True:
    #         raise ValidationError("Please correct email !")
    #     return self.cleaned_data['email']

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas !")
        return self.cleaned_data['confirm_password']

# class LoginForm(forms.Form):
#     username = forms.CharField(required=True, widget=forms.TextInput(attrs={
#         "placeholder": 'username'
#     }))
#     password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
#         "placeholder": 'password'
#     }))
#
#
# class Registration(forms.ModelForm):
#     confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password", "confirm_password")
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#
#     def clean_confirm_password(self):
#         if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
#             raise ValidationError("Parollar bir xil emas !")
#         return self.cleaned_data['confirm_password']
