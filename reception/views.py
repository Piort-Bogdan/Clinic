

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect


# from aspose.words import Document
# from docxtpl import DocxTemplate

from clients_data.models import Pets
from reception.forms import RecievRequestForm
from reception.models import Receptions, RecieveRequsetModel
from users.models import CustomUserForm,AbstractUser
from .tasks import recieve_order_created







def show_request(request):
        users = CustomUserForm
        Reception = Receptions.objects.all()
        return render(request, 'reception.html', {
            'Reception': Reception,
            'users': users
        })



def reception_request(request):
    """ Заявка на прием """
    if request.user.is_authenticated:
        owner_data = CustomUserForm.objects.get(id=request.user.id)
        pets = Pets.objects.get(id=request.user.owner_pet.id)
        if request.method == 'POST':
            form = RecievRequestForm(request.POST)
            print('Данные запроса', request.POST)
            print(form.is_valid())
            if form.is_valid():
                print(f'valid data : {form.cleaned_data}')
                form.save()
                reciev_id = RecieveRequsetModel.objects.filter(time_to_come=form.cleaned_data["time_to_come"], data_to_come=form.cleaned_data["data_to_come"]).get().id
                recieve_order_created.delay(reciev_id)

                return HttpResponse(f'<h1>Вы записались на {form.cleaned_data["time_to_come"]}, электронное подтверждение отправлено на Email {CustomUserForm.objects.get(id = request.POST.get("email_recive")).email}.</h1>')



        form = RecievRequestForm()
        return render(request, 'reception-request.html', {'form': form,
                                                            'owner_data': owner_data,
                                                            'pets': pets,
                                                            })
    else:
        form = RecievRequestForm()
        return render(request, 'reception-request.html', {'form': form,
                                                            })


