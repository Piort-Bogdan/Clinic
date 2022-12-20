from django.contrib import admin
from django.contrib.admin import display

from .models import Receptions, RecieveRequsetModel
from .models import CustomUserForm


# Register your models here.



@admin.register(Receptions)
class ReceptionsAdmin(admin.ModelAdmin):
    readonly_fields = ('kind_of_pet_rec', )
    list_display = ('owner_name', 'get_owner_lastname', 'data_receptions', 'doctor')




    def get_owner_lastname(self, obj):
       return obj.owner_lastname.objects.last_name.get()


    def get_job_title(self, obj):
       return obj.doctor.doctor_job_title.get()
#python manage.py shell_plus --print-sql



@admin.register(RecieveRequsetModel)
class RecieveRequsetModelAdmin(admin.ModelAdmin):
    list_display = ('owner_first_last_name', 'get_number', 'get_email', "get_name_kind", 'time_to_come', 'data_to_come', 'status')
    list_editable = ('status', )

    @display(description='Номер телефона')
    def get_number(self, obj):
        return obj.pet_owner.owner_tel


    @display(description='E-mail')
    def get_email(self, obj):
        return obj.pet_owner.email


    @display(description='ФИО')
    def owner_first_last_name(self, obj):
        return f'{obj.pet_owner.first_name} {obj.pet_owner.last_name} {obj.pet_owner.owner_fathername}'


    @display(description='Питомец')
    def get_name_kind(self, obj):
        return f'Кличка - {obj.pet_owner.owner_pet.pet_nickname}, Возраст - {obj.pet_owner.owner_pet.pet_age}, ' \
               f'вид: {obj.pet_owner.owner_pet.kind_of_pet.kind_of_pet}'









