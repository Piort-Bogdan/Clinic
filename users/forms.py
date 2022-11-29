from django import forms
from django.contrib.auth.models import AbstractUser





class RegisterForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    Email = forms.EmailField(label='Электронная почта', widget=forms.EmailField)




class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':  'form-input'}))
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
    )