from django.db import models

from production_calendar.models import CalendarDay
from users.models import UserProfile

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    calendar_day = models.ForeignKey(CalendarDay, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    lunch_break = models.IntegerField(blank=True, null=True, default=30)

    class Meta:
        unique_together = ('doctor', 'calendar_day')

    def __str__(self):
        return f'{self.doctor} schedule for {self.calendar_day}'            
