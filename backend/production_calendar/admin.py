from django.contrib import admin

from .models import (
    CalendarDay
    )


@admin.register(CalendarDay)
class CalendarDayAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in CalendarDay._meta.fields
        ]
