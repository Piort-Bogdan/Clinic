from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated, )


from .serializers import UserListSerializer
from users.models import CustomUserForm



class UserListView(generics.ListAPIView):
    queryset = CustomUserForm.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated,  ]


class UserCreateView(generics.ListCreateAPIView):
    queryset = CustomUserForm.objects.all()
    serializer_class = UserListSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomUserForm.objects.all()
    serializer_class = UserListSerializer


class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = CustomUserForm.objects.all()
    serializer_class = UserListSerializer



