from django.urls import path
from . import views

urlpatterns = [

  path('reception/', views.receptions, name='receptions'),
  path('reception-request/', views.reception_request, name='reception-request'),
  path('reception/api', views.reception_serializer.as_view()),




]