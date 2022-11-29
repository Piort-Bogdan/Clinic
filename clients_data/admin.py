from django.contrib import admin
from django.contrib.admin import display
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'doctor_lastname', 'doctor_fathername', 'get_img', 'job_title']
    readonly_fields = ('job_title', 'get_img' )



    @display(description='Должность')
    def job_title(self, obj):
        return obj.doctor_job_title



    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.doctor_foto.url}" width="80px"')

    get_img.short_description = 'Фото'


@admin.register(ClientsData)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'owner_lastname',  'pet_nickname', 'kind_of_pet', 'owner_adres', 'owner_tel', 'owner_email', 'owner_create_data')
admin.site.register(Pets)

admin.site.register(DoctorsJobTitle)
admin.site.register(KindOfPet)



