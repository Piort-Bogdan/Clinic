# Generated by Django 4.1.3 on 2022-11-20 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsJobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctors_job_title', models.CharField(max_length=100, verbose_name='Полная  должность врача')),
            ],
            options={
                'verbose_name': 'Должность врача',
                'verbose_name_plural': 'Должность врачей',
            },
        ),
        migrations.CreateModel(
            name='KindOfPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of_pet', models.CharField(max_length=20, null=True, verbose_name='Вид животного')),
            ],
            options={
                'verbose_name': 'Вид животного',
                'verbose_name_plural': 'Вид животного',
            },
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_nickname', models.CharField(max_length=50, verbose_name='Кличка животного')),
                ('pet_age', models.IntegerField(verbose_name='Возраст животного')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=30, verbose_name='Имя доктора')),
                ('doctor_lastname', models.CharField(max_length=50, verbose_name='Фамилия доктора')),
                ('doctor_fathername', models.CharField(max_length=50, verbose_name='Отчество доктора')),
                ('doctor_tel', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('doctor_email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('doctor_foto', models.ImageField(upload_to='clients_data/doctors', verbose_name='Фотография')),
                ('doctor_job_title', models.ManyToManyField(to='clients_data.doctorsjobtitle', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
            },
        ),
        migrations.CreateModel(
            name='ClientsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(help_text='Введите имя владельца', max_length=30, verbose_name='Имя владельца')),
                ('owner_lastname', models.CharField(max_length=50, verbose_name='Фамилия владельца')),
                ('owner_fathername', models.CharField(max_length=50, verbose_name='Отчетство владельца')),
                ('owner_adres', models.CharField(max_length=200, verbose_name='Адерс владельца')),
                ('owner_tel', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('owner_email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('owner_create_data', models.DateTimeField(auto_now_add=True, verbose_name='Время внесения данных')),
                ('pet_gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол животного')),
                ('kind_of_pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients_data.kindofpet', verbose_name='Вид животного')),
                ('pet_nickname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pet_nicknames', to='clients_data.pets', verbose_name='Кличка животного')),
            ],
            options={
                'verbose_name': 'Данные клиента',
                'verbose_name_plural': 'Данные клиентов',
            },
        ),
    ]
