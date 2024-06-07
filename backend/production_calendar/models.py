from django.db import models
from django.utils.translation import gettext_lazy as _

class CalendarDay(models.Model):
    date = models.DateField(unique=True)
    DAY_TYPES = [
        ('workday', _('Рабочий')),
        ('day_off', _('Выходной')),
        ('holiday', _('Праздничный')),
        ('pre_holiday', _('Предпраздничный')),
    ]
    day_type = models.CharField(max_length=20, choices=DAY_TYPES)
    work_hours = models.DecimalField(max_digits=4, decimal_places=2)
