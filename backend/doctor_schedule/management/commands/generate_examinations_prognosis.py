from datetime import timedelta
from django.core.management.base import BaseCommand
from django.db.models import Q
from core.prediction import arima, linear_regression, sarima, prophet
from production_calendar.models import ExaminationSchedule

DAY_COUNT = 365

class Command(BaseCommand):
    help = 'Predict the number of examinations'

    def add_arguments(self, parser):
        parser.add_argument('algorithm', type=str, help='Algorithm to use for prediction')

    def handle(self, *args, **kwargs):
        algorithm = kwargs['algorithm']
        last_day_with_actual_count = ExaminationSchedule.objects.filter(~Q(actual_count=None)).order_by('-day__date').first()
        start_date = last_day_with_actual_count.day.date + timedelta(days=1)

        if algorithm == 'linear':
            linear_regression(start_date, DAY_COUNT)
        elif algorithm == 'arima':
            arima(start_date, DAY_COUNT)
        elif algorithm == 'sarima':
            sarima(start_date, DAY_COUNT)            
        elif algorithm == 'prophet':
            prophet(start_date, DAY_COUNT)
        else:
            self.stdout.write(self.style.ERROR('Invalid algorithm'))

                        # Распределяем количество исследований по дням недели
                        # Хуй его знает, почему, но допустим, данных-то нет
                        # if day.date.weekday() < 5:  # Понедельник - Пятница
                        #     actual_count = int(examination_count) * 0.177
                        # elif day.date.weekday() == 5:  # Суббота
                        #     actual_count = int(examination_count) * 0.071
                        # else:  # Воскресенье
                        #     actual_count = int(examination_count) * 0.043
