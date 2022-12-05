from django.urls import path
from users import views
from .views import RegisterUser, ThanksPage

urlpatterns = [
  path('login/', views.user_login, name='login'),
  path('register/', RegisterUser.as_view(), name='register'),
  path('thanks/', ThanksPage, name='thanks')
]