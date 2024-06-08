from django.contrib import admin

from .models import (
    CalendarDay,
    OperatingMode,
    )


@admin.register(CalendarDay)
class CalendarDayAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in CalendarDay._meta.fields
        ]

@admin.register(OperatingMode)
class OperatingModeAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in OperatingMode._meta.fields
        ]
