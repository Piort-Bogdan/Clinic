from django.contrib import admin
from.models import Pharmacy, Medicine_Category, Medicine_Form


admin.site.register(Medicine_Form)

@admin.register(Medicine_Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug_category', ]
    prepopulated_fields = { 'slug_category': ('category', )}



@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = [ "title_medicine", 'manufacturer','expiration_data', 'count', 'category', 'price', ]
    list_filter = [ 'expiration_data', 'count', ]
    list_editable = [ 'price', ]
    prepopulated_fields = { 'slug': ('title_medicine', )}