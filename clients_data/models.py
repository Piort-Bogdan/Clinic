from django.db import models




class KindOfPet(models.Model):
    kind_of_pet = models.CharField('Вид животного', max_length=20, null=True)

    def __str__(self):
        return f'{self.kind_of_pet}'

    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Вид животного'



class Pets(models.Model):
    GENDER = {
        ("m",'Мужской'),
        ('f','Женский')
    }

    pet_nickname = models.CharField('Кличка животного', max_length=50)
    pet_age = models.IntegerField('Возраст животного')
    pet_nickname = models.CharField('Кличка животного', max_length=100)
    kind_of_pet = models.ForeignKey(KindOfPet,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    verbose_name='Вид животного'
                                    )
    pet_gender = models.CharField('Пол животного', max_length=1, choices=GENDER)

    def __str__(self):
        return f'{self.pet_nickname}'

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class DoctorsJobTitle(models.Model):
    doctors_job_title = models.CharField(verbose_name='Полная  должность врача', max_length=100)

    def __str__(self):
        return self.doctors_job_title

    class Meta:
        verbose_name = 'Должность врача'
        verbose_name_plural = 'Должность врачей'


class Doctors(models.Model):
    doctor_name = models.CharField('Имя доктора', max_length=30)
    doctor_lastname = models.CharField('Фамилия доктора', max_length=50)
    doctor_fathername = models.CharField('Отчество доктора', max_length=50)
    doctor_tel = models.CharField('Номер телефона', max_length=30)
    doctor_email = models.EmailField('Электронная почта')
    doctor_foto = models.ImageField('Фотография', upload_to='clients_data/doctors')
    doctor_job_title = models.ManyToManyField(DoctorsJobTitle, verbose_name='Должность')




    def __str__(self):
        return self.doctor_name

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'






