from django.contrib import admin

from .models import (
    CalendarDay,
    OperatingMode,
    ExaminationSchedule,
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

@admin.register(ExaminationSchedule)
class ExaminationScheduleAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in ExaminationSchedule._meta.fields
        ]
