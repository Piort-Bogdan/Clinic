from django.db import models
from clients_data.admin import DoctorsAdmin

from clients_data.models import Doctors, KindOfPet, Pets, DoctorsJobTitle
from users.models import CustomUserForm

from clients_data.models import ClientsData, Doctors, KindOfPet, Pets, DoctorsJobTitle





class Receptions(models.Model):

    owner_name = models.ForeignKey(CustomUserForm, verbose_name='Имя владельца', on_delete=models.CASCADE, null=True,
                                   related_name='owners')
    owner_lastname_rec = models.ForeignKey(CustomUserForm, verbose_name='Фамилия владельца', on_delete=models.CASCADE,
                                           null=True)
    kind_of_pet_rec = models.ForeignKey(KindOfPet, verbose_name='Вид животного', on_delete=models.SET_NULL, null=True,
                                        related_name='Kinde_pets')
    pet_gender_rec = models.ForeignKey(KindOfPet, verbose_name='Вид животного', on_delete=models.SET_NULL, null=True,
                                       related_name='+')
    pet_nickname_rec = models.ForeignKey(Pets, verbose_name='Кличка животного', on_delete=models.CASCADE, null=True,
                                         related_name='nick_names')
    data_receptions = models.DateTimeField(auto_now_add =True, verbose_name='Дата приема')
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True)
    doctor_job_title_rec = models.ForeignKey(DoctorsJobTitle, on_delete=models.SET_NULL, null=True,
                                             related_name='job_titles')
    rec_diagnose = models.CharField('Диагноз', max_length=100)
    rec_instructions = models.TextField('Указания')
    owner_email = models.ForeignKey(CustomUserForm, verbose_name="Электронная почта", on_delete=models.SET_NULL,
                                    blank=True, null=True, related_name='Owner_emails')
    owner_name = models.ForeignKey(ClientsData, verbose_name='Имя владельца', on_delete=models.CASCADE, null=True,
                                   related_name='owners')
    owner_lastname_rec = models.ForeignKey(ClientsData, verbose_name='Фамилия владельца', on_delete=models.CASCADE,
                                           null=True)
    kind_of_pet_rec = models.ForeignKey(KindOfPet, verbose_name='Вид животного', on_delete=models.SET_NULL, null=True,
                                        related_name='Kinde_pets')
    pet_gender_rec = models.ForeignKey(ClientsData, verbose_name='Вид животного', on_delete=models.SET_NULL, null=True,
                                       related_name='+')
    pet_nickname_rec = models.ForeignKey(Pets, verbose_name='Кличка животного', on_delete=models.CASCADE, null=True,
                                         related_name='nick_names')
    data_receptions = models.DateTimeField(auto_now_add =True, verbose_name='Дата приема')
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True)
    doctor_job_title_rec = models.ForeignKey(DoctorsJobTitle, on_delete=models.SET_NULL, null=True,
                                             related_name='job_titles')
    rec_diagnose = models.CharField('Диагноз', max_length=100)
    rec_instructions = models.TextField('Указания')
    rec_medicine = models.ManyToManyField('pet_pharmacy.Pharmacy', blank=True, verbose_name='Назначенные лекарств')


    def __str__(self):
        return f'Прием пациента - {self.pet_nickname_rec}, Владелец - {self.owner_name} {self.owner_lastname_rec.owner_lastname}, Врач - {self.doctor} {self.doctor.doctor_lastname}'


    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'


