from django.contrib import admin

from .models import (
    Modality,
    )


@admin.register(Modality)
class ModalityAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Modality._meta.fields
        ]
