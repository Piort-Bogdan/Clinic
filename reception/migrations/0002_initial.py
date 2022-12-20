# Generated by Django 4.1.3 on 2022-12-16 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet_pharmacy', '0001_initial'),
        ('clients_data', '0001_initial'),
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recieverequsetmodel',
            name='email_recive',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails_recieve', to=settings.AUTH_USER_MODEL, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='recieverequsetmodel',
            name='pet_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pets_name', to=settings.AUTH_USER_MODEL, verbose_name='Имя питомца'),
        ),
        migrations.AddField(
            model_name='recieverequsetmodel',
            name='pet_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='recieverequsetmodel',
            name='tel_num',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tel', to=settings.AUTH_USER_MODEL, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients_data.doctors'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='doctor_job_title_rec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_titles', to='clients_data.doctorsjobtitle'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='kind_of_pet_rec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Kinde_pets', to='clients_data.kindofpet', verbose_name='Вид животного'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='owner_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Owner_emails', to=settings.AUTH_USER_MODEL, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='owner_lastname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Фамилия владельца'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='owner_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL, verbose_name='Имя владельца'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='pet_gender_rec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='clients_data.kindofpet', verbose_name='Вид животного'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='pet_nickname_rec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nick_names', to='clients_data.pets', verbose_name='Кличка животного'),
        ),
        migrations.AddField(
            model_name='receptions',
            name='rec_medicine',
            field=models.ManyToManyField(blank=True, to='pet_pharmacy.pharmacy', verbose_name='Назначенные лекарств'),
        ),
    ]
