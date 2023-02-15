


from django.http import HttpResponse
from django.shortcuts import render


from clients_data.models import Pets
from reception.forms import RecievRequestForm, RecieveForm
from reception.models import Receptions, RecieveRequsetModel
from users.models import CustomUserForm
from reception.tasks import recieve_order_created, RecievDocs








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
                reciev_id = RecieveRequsetModel.objects.filter(time_to_come=form.cleaned_data["time_to_come"],
                                                               data_to_come=form.cleaned_data["data_to_come"]).get().id
                print('id:', reciev_id)
                recieve_order_created.delay(reciev_id)
                # print('gjg', recieve_order_created(reciev_id) )

                return HttpResponse(f'<h1>Вы записались на {form.cleaned_data["time_to_come"]}, '
                                    f'электронное подтверждение отправлено на Email '
                                    f'{CustomUserForm.objects.get(id = request.POST.get("email_recive")).email}.</h1>')



        form = RecievRequestForm()
        return render(request, 'reception-request.html', {'form': form,
                                                            'owner_data': owner_data,
                                                            'pets': pets,
                                                            })
    else:
        form = RecievRequestForm()
        return render(request, 'reception-request.html', {'form': form,
                                                            })





def receptions(request):

    """ Данные для PDF версии приема, для отправки на почту клиенту после приема """

    recieve_data = RecieveRequsetModel.objects.filter(status = 'CONFIRMED')
    doctor_data = CustomUserForm.objects.filter(id=request.user.id)
    print(request.user.id)
    print(request.POST)



        # if request.user.is_staff:
    if request.method == 'POST':
        form = RecieveForm(request.POST)
        print('Данные реквеста:', request.POST)
        if form.is_valid():
            print('Данные из формы: ', form.cleaned_data)
            form.save()
            print(Receptions.objects.filter(rec_instructions=form.cleaned_data['rec_instructions']).get().send_pdf_reciev_copy)
            if Receptions.objects.filter(rec_instructions=form.cleaned_data['rec_instructions']).get().send_pdf_reciev_copy:
                pdf_data = Receptions.objects.filter(rec_instructions=form.cleaned_data['rec_instructions']).get().id
                RecievDocs.delay(pdf_data)
            return render (request, 'reception.html', {'recieve_data': recieve_data,
                                                        'doctor_data': doctor_data,
                                                        'form': form})


    form = RecieveForm()
    return render(request, 'reception.html', {'recieve_data': recieve_data,
                                                   'doctor_data': doctor_data,
                                              'form': form})



    # def reception_pdf_data(self, request):


