from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModalityViewSet, MedicalExaminationViewSet

app_name = 'medical_examination'
router = DefaultRouter()
router.register(r'modalities', ModalityViewSet)
router.register(r'medical_examination', MedicalExaminationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]