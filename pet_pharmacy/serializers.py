from rest_framework import serializers

from .models import *


class PharmacyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

