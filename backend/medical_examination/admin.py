from django.contrib import admin

from .models import (
    Modality,
    MedicalExamination
    )


@admin.register(Modality)
class ModalityAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Modality._meta.fields
        ]

@admin.register(MedicalExamination)
class MedicalExaminationAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in MedicalExamination._meta.fields
        ]
