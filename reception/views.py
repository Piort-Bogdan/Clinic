from django.shortcuts import render
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

