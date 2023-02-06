# Generated by Django 4.1.3 on 2023-01-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0016_alter_recieverequsetmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recieverequsetmodel',
            name='status',
            field=models.CharField(choices=[('NULL', 'Анулированна'), ('CONFIRMED', 'Подтверждено'), ('CANCELED', 'Отменена'), ('NEW', 'Новая заявка'), ('FINISH', 'Готово'), ('IN_PROCESS', 'В процессе')], default='Новая заявка', max_length=12),
        ),
    ]