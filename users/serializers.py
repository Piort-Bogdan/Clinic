from rest_framework import serializers

from users.models import CustomUserForm


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserForm
        fields = ('username', 'password',)

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)

        user.set_password(user.password)
        user.save()

        return user

