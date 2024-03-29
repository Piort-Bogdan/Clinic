# Generated by Django 4.1.3 on 2023-01-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recieverequsetmodel',
            name='reception_pdf',
            field=models.FileField(blank=True, null=True, upload_to='recievs/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='recieverequsetmodel',
            name='status',
            field=models.CharField(choices=[('IN_PROCESS', 'В процессе'), ('NULL', 'Анулированна'), ('FINISH', 'Готово'), ('NEW', 'Новая заявка'), ('CONFIRMED', 'Подтверждено'), ('CANCELED', 'Отменена')], default='Новая заявка', max_length=12),
        ),
    ]
