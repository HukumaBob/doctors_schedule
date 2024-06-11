from django.contrib import admin

from .models import (
    PredictionTuning
)


@admin.register(PredictionTuning)
class PredictionTuningAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in PredictionTuning._meta.fields
        ]
