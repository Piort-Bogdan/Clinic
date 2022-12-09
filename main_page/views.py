from django.shortcuts import render
from clients_data.models import *


def main_page(request):

    main_data = {
        'id':id
    }
    return render(request, 'main/main.html', {})
