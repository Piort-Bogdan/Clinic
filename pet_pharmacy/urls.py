from django.urls import path
from . import views

urlpatterns = [

  path('pharmacy/', views.PharmacyList.as_view(), name='pharmacy-list'),
  path('pharmacy-create/', views.PharmacyCreate.as_view(), name='pharmacy-create'),
  path('pharmacy-update/<int:pk>', views.PharmacyUpdate.as_view(), name='pharmacy-update'),
  path('pharmacy-shop/', views.pharmacy_shop_list),
  path('pharmacy-shop/<slug:slug>', views.pharmacy_product_detail),





]