# Generated by Django 4.1.3 on 2022-12-03 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='kind_of_pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients_data.kindofpet', verbose_name='Вид животного'),
        ),
    ]
