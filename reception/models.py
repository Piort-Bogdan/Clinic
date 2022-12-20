from django.db import models
from users.models import CustomUserForm
from clients_data.models import Doctors, KindOfPet, Pets, DoctorsJobTitle





class Receptions(models.Model):

    '''Данные дял проведения приема'''

    owner_name = models.ForeignKey(CustomUserForm, verbose_name='Имя владельца', on_delete=models.CASCADE, null=True,
                                   related_name='owners')
    owner_lastname = models.ForeignKey("users.CustomUserForm", verbose_name='Фамилия владельца', on_delete=models.CASCADE,
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
    rec_medicine = models.ManyToManyField('pet_pharmacy.Pharmacy', blank=True, verbose_name='Назначенные лекарств')


    def __str__(self):
        return f'Прием пациента - {self.pet_nickname_rec}, Владелец - {self.owner_name} {self.owner_lastname_rec.owner_lastname}, Врач - {self.doctor} {self.doctor.doctor_lastname}'


    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'






class RecieveRequsetModel(models.Model):

    '''Данные для формы записи на прием'''

    STATUS = {
        ('NEW', 'Новая заявка'),
        ('CONFIRMED', 'Подтверждено'),
        ('IN_PROCESS', 'В процессе'),
        ('NULL', 'Анулированна'),
        ('CANCELED', 'Отменена'),
        ('FINISH', 'Готово'),
    }

    pet_owner = models.ForeignKey("users.CustomUserForm", verbose_name='Владелец',
                                  on_delete=models.CASCADE, blank=True, null=True)
    derscription = models.TextField(verbose_name='Описание проблемы')
    email_recive = models.ForeignKey("users.CustomUserForm", verbose_name='Электронная почта',
                                     on_delete=models.CASCADE, null=True, related_name='emails_recieve')
    tel_num = models.ForeignKey("users.CustomUserForm", verbose_name='Номер телефона',
                                on_delete=models.CASCADE, null=True, related_name='tel')
    data_to_come = models.DateField(verbose_name='Дата записи')
    time_to_come = models.TimeField(verbose_name='Время записи')
    pet_name = models.ForeignKey("clients_data.Pets", verbose_name='Имя питомца',
                                 on_delete=models.CASCADE, null=True, related_name='Pets_name')
    status = models.CharField(max_length=12, choices=STATUS, default='Новая заявка')


    def __str__(self):
        return str(self.pet_owner)


    class Meta:
        verbose_name = 'Заявка на прием'
        verbose_name_plural = 'Заявки на прием'





