from django.db import models
from django.utils.translation import gettext_lazy as _
from medical_examination.models import MedicalExamination

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

    def __str__(self):
        return str(self.date)    

class OperatingMode(models.Model):
    code = models.IntegerField(primary_key=True)
    operating_mode = models.CharField(max_length=50)

    def __str__(self):
        return self.operating_mode    
    
class ExaminationSchedule(models.Model):
    day = models.ForeignKey(CalendarDay, on_delete=models.CASCADE)
    examination = models.ForeignKey(MedicalExamination, on_delete=models.CASCADE)
    predicted_count = models.IntegerField(null=True, blank=True)
    actual_count = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('day', 'examination')