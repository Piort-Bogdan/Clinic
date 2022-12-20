from django.urls import path
from users import views


urlpatterns = [
  path('auth/api/users/', views.UserListView.as_view()),
  path('auth/api/create/', views.UserCreateView.as_view()),
  path('auth/api/update/<int:pk>', views.UserUpdateView.as_view()),
  path('auth/api/delete/<int:pk>', views.UserDeleteView.as_view())
  ]





