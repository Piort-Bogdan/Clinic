from django.shortcuts import render
from rest_framework import generics
from .models import  Pharmacy
from .serializers import PharmacyListSerializer

class PharmacyList(generics.ListAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyListSerializer


class PharmacyCreate(generics.CreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyListSerializer

class PharmacyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyListSerializer



