from django.contrib import admin
from django.contrib.admin import display

import clients_data.models
import reception.models
from clients_data.models import Doctors
from .models import Receptions
from clients_data.models import DoctorsJobTitle

# Register your models here.



@admin.register(Receptions)
class ReceptionsAdmin(admin.ModelAdmin):
    readonly_fields = ('kind_of_pet_rec', )
    list_display = ('owner_name', 'get_owner_lastname', 'data_receptions', 'doctor')


    def get_owner_lastname(self, obj):
       return obj.owner_lastname_rec.owner_lastname


    def get_job_title(self, obj):
       return obj.doctor.doctor_job_title.get()
#python manage.py shell_plus 7--print-sql