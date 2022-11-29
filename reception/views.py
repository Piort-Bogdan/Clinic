from django.shortcuts import render
from clients_data.models import Doctors, ClientsData
from reception.models import Receptions


def show_request(request):
    Doctor = Doctors.objects.all()
    Owner = ClientsData.objects.all()


    return render(request, 'reception.html', {
        'Doctor': Doctor,
        'Owner': Owner,
    })
