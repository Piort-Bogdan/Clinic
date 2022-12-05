from django.db import models
from django.contrib.auth.models import AbstractUser
from clients_data.models import KindOfPet, Pets




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
                                  null=True
                                  )
    owner_tel = models.CharField('Номер телефона',
                                 max_length=30
                                 )

    owner_name = models.CharField('Имя владельца',
                                  max_length=30,
                                  help_text='Введите имя владельца'
                                  )
    owner_lastname = models.CharField('Фамилия владельца',
                                      max_length=50
                                      )
    owner_fathername = models.CharField('Отчество владельца',
                                        max_length=50
                                        )


