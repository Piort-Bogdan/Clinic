from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserForm





class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUserForm
        fields = ('owner_name', 'owner_lastname', 'owner_fathername', 'owner_tel', 'gender', 'username', 'email' )


=======
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90



class LoginForm(forms.Form):
<<<<<<< HEAD
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':  'form-input'}))
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
=======
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90
    )