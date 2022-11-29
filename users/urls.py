from django.urls import path
from users import views
from .views import RegisterUser



urlpatterns = [
  path('login/', views.user_login, name='login'),
  path('register/', RegisterUser, name='register')
]