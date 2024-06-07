import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from production_calendar.models import CalendarDay

class Command(BaseCommand):
    help = 'Load a work calendar csv file into the database'

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(
            settings.BASE_DIR / f'data/work_calendar2022-2024.csv', 'r', encoding='utf-8'
                ) as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                _, created = CalendarDay.objects.get_or_create(
                    date=row[0],
                    day_type=row[3],
                    work_hours=row[4]
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{'Successfully added' if created else 'Already exists'}: {row[0]} - {row[3]} - {row[4]}"
                    )
                )
