from django.urls import path
<<<<<<< HEAD
from users import views
from .views import RegisterUser, ThanksPage

urlpatterns = [
  path('login/', views.user_login, name='login'),
  path('register/', RegisterUser.as_view(), name='register'),
  path('thanks/', ThanksPage, name='thanks')
=======
from django.contrib.auth import views



urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login')
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90
]