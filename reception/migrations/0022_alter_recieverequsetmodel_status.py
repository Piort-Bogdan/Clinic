# Generated by Django 4.1.3 on 2023-02-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0021_alter_recieverequsetmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieverequsetmodel',
            name='status',
            field=models.CharField(choices=[('NULL', 'Анулированна'), ('NEW', 'Новая заявка'), ('CONFIRMED', 'Подтверждено'), ('CANCELED', 'Отменена'), ('FINISH', 'Готово'), ('IN_PROCESS', 'В процессе')], default='Новая заявка', max_length=12),
        ),
    ]