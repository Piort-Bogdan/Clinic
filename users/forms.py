from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserForm





class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUserForm
        fields = ('owner_name', 'owner_lastname', 'owner_fathername', 'owner_tel', 'gender', 'username', 'email' )






class LoginForm(forms.Form):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':  'form-input'}))
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )