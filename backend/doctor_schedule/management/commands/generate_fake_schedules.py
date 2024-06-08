import random
from datetime import datetime, time, timedelta, date
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from users.models import UserProfile
from doctor_schedule.schedule_generation import generate_schedule

class Command(BaseCommand):
    help = 'Generate schedules for doctors'

    def handle(self, *args, **options):
        # Получаем всех врачей
        doctors = UserProfile.objects.filter(position='doctor')

        # Устанавливаем начальную и конечную даты
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=90)  # 3 месяца вперед

        # Устанавливаем время начала работы
        start_times = [time(9, 0), time(12, 0)]  # 9:00 или 12:00

        for doctor in doctors:
            # Выбираем произвольное время начала работы для каждого врача
            start_time = random.choice(start_times)

            # Генерируем расписание для врача
            generate_schedule(doctor, start_date, end_date, start_time)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Расписание для {doctor.user.username} успешно создано."
                )
            )
