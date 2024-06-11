from rest_framework import viewsets
from .models import Modality, MedicalExamination
from .serializers import ModalitySerializer, MedicalExaminationSerializer

class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer

class MedicalExaminationViewSet(viewsets.ModelViewSet):
    queryset = MedicalExamination.objects.all()
    serializer_class = MedicalExaminationSerializer
