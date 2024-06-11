# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

app_name = 'users'
# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile_detail'),
]
