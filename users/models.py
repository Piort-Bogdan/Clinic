
from django.db import models
from django.contrib.auth.models import AbstractUser

from clients_data.models import DoctorsJobTitle


class CustomUserForm(AbstractUser):
    GENDERS = {
        ('m',"Мужской"),
        ('f',"Женский")
    }

    gender=models.CharField(max_length=1,
                            choices=GENDERS,
                            default="",
                            verbose_name="Пол"
                            )
    owner_pet = models.ForeignKey("clients_data.Pets",
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True,
                                  )
    owner_tel = models.CharField('Номер телефона',
                                 max_length=30
                                 )

    owner_fathername = models.CharField('Отчество владельца',
                                        max_length=50
                                        )

    doctor_foto = models.ImageField('Фотография', upload_to='clients_data/doctors', blank=True)
    doctor_job_title = models.ManyToManyField(DoctorsJobTitle, verbose_name='Должность', blank=True)

