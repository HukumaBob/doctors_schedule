# views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.serializers import  UserProfileSerializer
from users.models import User, UserProfile
from .filters import UserProfileFilter

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserProfileFilter
