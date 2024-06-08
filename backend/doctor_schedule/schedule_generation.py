from datetime import datetime, time, timedelta, date
from django.core.exceptions import ValidationError

from users.models import UserProfile
from .models import DoctorSchedule
from production_calendar.models import CalendarDay, OperatingMode

def create_schedule(doctor, calendar_day, start_time, end_time):
    """
    Создает расписание, если такого еще нет.
    """
    schedule, created = DoctorSchedule.objects.get_or_create(
        doctor=doctor,
        calendar_day=calendar_day,
        defaults={'start_time': start_time, 'end_time': end_time},
    )
    return schedule

def generate_schedule(doctor: UserProfile, start_date: date, end_date: date, start_time: time):
    """
    Функция генерирует расписание работы врача в зависимости от режима работы и сохраняет его в базе данных.
    """
    operating_mode = doctor.operating_mode
    wage_rate = doctor.wage_rate
    hours_worked = int(wage_rate * 8)
    end_time = (datetime.combine(date.today(), start_time) + timedelta(hours=hours_worked)).time()

    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValidationError('Start and end dates must be datetime.date instances.')
    if not (0 < wage_rate <= 1.25):
        raise ValidationError('Wage rate must be between 0 and 1.25.')
    if operating_mode.code not in OperatingMode.objects.values_list('code', flat=True):
        raise ValidationError('Invalid operating mode.')

    current_date = start_date
    while current_date <= end_date:
        if operating_mode.code in [10, 11] and current_date.weekday() < operating_mode.code % 10:
            calendar_day = CalendarDay.objects.get(date=current_date)
            create_schedule(doctor, calendar_day, start_time, end_time)
        elif operating_mode.code == 20 and (current_date - start_date).days % 4 < 2:
            calendar_day = CalendarDay.objects.get(date=current_date)
            create_schedule(doctor, calendar_day, start_time, end_time)
        current_date += timedelta(days=1)
