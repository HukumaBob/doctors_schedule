import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from medical_examination.models import MedicalExamination
from production_calendar.models import CalendarDay, ExaminationSchedule
from datetime import datetime, timedelta
       

class Command(BaseCommand):
    help = 'Fill ExaminationSchedule model'

    def handle(self, *args, **options):
        # Открываем CSV-файл
        with open(
            settings.BASE_DIR / f'data/examinations_statistic2022_2024.csv', 'r', encoding='utf-8'
                ) as f: 
            reader = csv.reader(f)
            headers = next(reader)  # Читаем заголовок
            examination_codes = headers[2:]  # Получаем коды исследований

            # Создаем словарь для хранения данных из CSV
            csv_data = {}
            for row in reader:
                year, week, *examinations = row
                start_date = datetime.strptime(f'{year}-W{int(week)-1}-1', "%Y-W%W-%w").date()
                for i in range(7):  # Для каждого дня недели
                    date = start_date + timedelta(days=i)
                    csv_data[date] = examinations

            # Перебираем все дни в CalendarDay и все медицинские обследования
            for day in CalendarDay.objects.all():
                for code in examination_codes:
                    examination = MedicalExamination.objects.get(code=int(code))
                    examinations = csv_data.get(day.date)
                    if examinations is not None:
                        examination_count = examinations[examination_codes.index(code)]
                        actual_count = int(examination_count)/7
                    else:
                        actual_count = None  # Если данных нет, устанавливаем actual_count в None

                    # Создаем новый объект ExaminationSchedule
                    schedule, created = ExaminationSchedule.objects.update_or_create(
                        day=day, 
                        examination=examination, 
                        defaults={'actual_count': actual_count}
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully created ExaminationSchedule for {day.date}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Successfully updated ExaminationSchedule for {day.date}'))

        self.stdout.write(self.style.SUCCESS('Successfully filled ExaminationSchedule model'))
