<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-12-09 12:51
=======
# Generated by Django 4.1.3 on 2022-11-20 23:09
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_receptions', models.DateTimeField(auto_now_add=True, verbose_name='Дата приема')),
                ('rec_diagnose', models.CharField(max_length=100, verbose_name='Диагноз')),
                ('rec_instructions', models.TextField(verbose_name='Указания')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients_data.doctors')),
<<<<<<< HEAD
                ('doctor_job_title_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_titles', to='clients_data.doctorsjobtitle')),
                ('kind_of_pet_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Kinde_pets', to='clients_data.kindofpet', verbose_name='Вид животного')),
=======
                ('doctor_job_title_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='clients_data.doctors')),
                ('kind_of_pet_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='clients_data.kindofpet', verbose_name='Вид животного')),
                ('owner_lastname_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients_data.clientsdata', verbose_name='Фамилия владельца')),
                ('owner_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='clients_data.clientsdata', verbose_name='Имя владельца')),
                ('pet_gender_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='clients_data.clientsdata', verbose_name='Вид животного')),
                ('pet_nickname_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clients_data.pets', verbose_name='Кличка животного')),
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90
            ],
            options={
                'verbose_name': 'Прием',
                'verbose_name_plural': 'Приемы',
            },
        ),
    ]
