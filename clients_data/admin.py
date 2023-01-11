from django.contrib import admin
from django.contrib.admin import display
from django.utils.safestring import mark_safe

from .models import *




admin.site.register(Pets)

admin.site.register(DoctorsJobTitle)
admin.site.register(KindOfPet)



