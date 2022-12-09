from django.shortcuts import render
<<<<<<< HEAD
from clients_data.models import Doctors
from reception.models import Receptions
from users.models import CustomUserForm,AbstractUser
from django.contrib.auth import authenticate, login



def show_request(request):
        users = CustomUserForm
        Reception = Receptions.objects.all()
        return render(request, 'reception.html', {
            'Reception': Reception,
            'users': users
        })
=======

# Create your views here.
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90
