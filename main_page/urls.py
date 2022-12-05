from django.urls import path

from main_page import views




urlpatterns = [

    path('main/', views.main_page, name='main_page')

]