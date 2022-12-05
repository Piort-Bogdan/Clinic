from django.shortcuts import render
from clients_data.models import Doctors
from reception.models import Receptions


def show_request(request):
    Doctor = Doctors.objects.all()



    return render(request, 'reception.html', {
        'Doctor': Doctor,
    })
