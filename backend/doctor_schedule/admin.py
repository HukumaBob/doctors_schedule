from django.contrib import admin

from .models import (
    DoctorSchedule,
    )


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in DoctorSchedule._meta.fields
        ]

