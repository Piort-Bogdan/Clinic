# Generated by Django 4.1.3 on 2023-01-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0011_alter_recieverequsetmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieverequsetmodel',
            name='status',
            field=models.CharField(choices=[('IN_PROCESS', 'В процессе'), ('CANCELED', 'Отменена'), ('CONFIRMED', 'Подтверждено'), ('FINISH', 'Готово'), ('NEW', 'Новая заявка'), ('NULL', 'Анулированна')], default='Новая заявка', max_length=12),
        ),
    ]
