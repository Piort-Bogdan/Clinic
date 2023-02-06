# Generated by Django 4.1.3 on 2023-01-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuserform_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserform',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], default='', max_length=1, verbose_name='Пол'),
        ),
    ]