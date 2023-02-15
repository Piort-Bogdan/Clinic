from django.contrib import admin
from django.contrib.admin import display
from django.forms import inlineformset_factory

from .models import Receptions, RecieveRequsetModel
from users.models import CustomUserForm

# Register your models here.


# class ReceptionsInLine(admin.TabularInline):
#     model = CustomUserForm




@admin.register(Receptions)
class ReceptionsAdmin(admin.ModelAdmin):
    readonly_fields = ('kind_of_pet_rec', 'id',  )
    list_display = ('get_owner_lastname', 'get_tel', 'data_receptions', 'doctor', 'id', )


    FriendshipFormSet = inlineformset_factory(CustomUserForm, RecieveRequsetModel, fk_name='email_recive',
    fields = ('tel_num', 'email_recive', 'pet_owner', ))

    def get_tel(self, obj):
        return obj.owner_name.owner_tel


    def get_owner_lastname(self, obj):
       return f'{obj.owner_name.first_name} {obj.owner_name.last_name}'


    def get_job_title(self, obj):
       return obj.doctor.doctor_job_title.doctors_job_title
#python manage.py shell_plus --print-sql




@admin.register(RecieveRequsetModel)
class RecieveRequsetModelAdmin(admin.ModelAdmin):
    list_display = ('owner_first_last_name', 'get_number', 'get_email', "get_name_kind", 'time_to_come', 'data_to_come', 'status')
    list_editable = ('status', )
    list_filter = ('status', 'data_to_come')
    search_fields = ('pet_owner__first_name__icontains', 'pet_name__pet_nickname__icontains' )
    list_per_page = 20


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









