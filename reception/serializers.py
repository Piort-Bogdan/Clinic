from rest_framework import serializers

from users.models import CustomUserForm
from .models import Receptions


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserForm
        fields = ("first_name", )


class ReceptionSerializer(serializers.ModelSerializer):
    # name = OwnerSerializer()

    class Meta:
        fields = ('owner_name', 'owner_lastname',  'kind_of_pet_rec', 'pet_gender_rec', 'pet_nickname_rec', 'data_receptions')
        model = Receptions
        depth = 1
