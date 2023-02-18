
from celery import shared_task
from django.core.mail import send_mail
from docx import Document

from .models import RecieveRequsetModel, Receptions


@shared_task
def recieve_order_created(receive_id):


    """"Отправка сообщений на майл владельца питомца с данными о записи на прием"""


    recieve = RecieveRequsetModel.objects.get(id=receive_id)
    mail_sent = send_mail(
        subject='Запись на прием в клинику "MOLLI"',
        message=f'Добрый день, Вы записались на прием {recieve.data_to_come} в '
                f'{recieve.time_to_come}',
        from_email='dominiusd@mail.ru',
        recipient_list=('dominiusd@mail.ru', ),
        fail_silently=False,
    )
    return mail_sent







@shared_task
def reciev_docs(pdf_data):
    from docxtpl import DocxTemplate
    from docx2pdf import convert

    RecievDoc = DocxTemplate('reception/doc-pdf-fuller/Vet_card_01.docx')
    context = {
        'Doctor': Receptions.objects.filter(id = pdf_data).get().doctor,
        'first_name': Receptions.objects.filter(id = pdf_data).get().owner_name,
        'last_name': Receptions.objects.filter(id = pdf_data).get().owner_lastname,
        'data': Receptions.objects.filter(id = pdf_data).get().data_receptions,
        'pet_name': Receptions.objects.filter(id = pdf_data).get().pet_nickname_rec,
    }
    RecievDoc.render(context)
    RecievDoc.save(f'reception/doc-pdf-fuller/Vet_card_{context["last_name"]}_{context["data"]}.docx')
    #Convert to pdf
    convert(f'reception/doc-pdf-fuller/Vet_card_{context["last_name"]}_{context["data"]}.docx',
            f'reception/doc-pdf-fuller/Vet_card_{context["last_name"]}_{context["data"]}.pdf')

