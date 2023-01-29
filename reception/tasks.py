from celery import shared_task
from django.core.mail import send_mail

from .models import RecieveRequsetModel




@shared_task
def recieve_order_created(receive_id):


    """"Отправка сообщений на майл владельца питомца с данными о записи на прием"""


    recieve = RecieveRequsetModel.objects.get(id=receive_id)
    mail_sent = send_mail(
        subject='Запись на прием в клинику "MOLLI"',
        message=f'Добрый день, Вы записались на прием {recieve.data_to_come} в '
                f'{recieve.time_to_come}',
        from_email='dominiusd@mail.ru',
        recipient_list=(recieve.objects.get(id=receive_id).email, ),
        fail_silently=False,
    )
    return mail_sent


