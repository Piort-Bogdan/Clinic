from django.urls import path
from . import views

urlpatterns = [

  path('reception/', views.show_request, name='receptions')


]