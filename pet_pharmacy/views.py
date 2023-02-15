from django.shortcuts import render, get_object_or_404
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



def pharmacy_shop_list(request):

    products = Pharmacy.objects.filter(count__gt=0)
    context = {
        'products' : products
    }
    return render(request, './Pharmacy/pharmacy_list.html', context)



def pharmacy_product_detail(request, slug):
    product = get_object_or_404(Pharmacy,
                                slug=slug,
                                count__gt = 0
                                )
    return render(request, './Pharmacy/pharmacy_detail.html', {'product': product})


# def pharmacy_product_list(request)