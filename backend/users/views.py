# views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from users.serializers import  UserProfileSerializer
from users.models import User, UserProfile
from .filters import UserProfileFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserProfileFilter
