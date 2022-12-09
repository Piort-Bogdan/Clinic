# Generated by Django 4.1.3 on 2022-11-25 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients_data', '0001_initial'),
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptions',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients_data.doctorsjobtitle'),
        ),
        migrations.AlterField(
            model_name='receptions',
            name='doctor_job_title_rec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_title', to='clients_data.doctors'),
        ),
    ]