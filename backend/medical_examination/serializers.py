from rest_framework import serializers
from .models import Modality, MedicalExamination

class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ['id', 'modality_specialization', 'modality']

class MedicalExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalExamination
        fields = ['code', 'examination_modality', 'examination_type', 'conventional_units']
