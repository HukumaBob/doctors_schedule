import csv
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from medical_examination.models import Modality
from users.models import Specialization
from medical_examination.models import MedicalExamination

class Command(BaseCommand):
    help = _('Загрузить CSV-файлы модальности и специализации в базу данных')

    def handle(self, *args, **options):
        # Обработка файла specialization.csv
        with open(
            settings.BASE_DIR / f'data/specialization.csv', 'r', encoding='utf-8'
                ) as f:
            reader = csv.reader(f)
            next(reader)  # Пропустить строку заголовка.
            for row in reader:
                specialization, created = Specialization.objects.get_or_create(
                    code=row[1],
                    specialization=row[0]
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{_('Успешно добавлено') if created else _('Уже существует')}: {row[0]} - {row[1]}"
                    )
                )

        # Обработка файла modality.csv
        with open(
            settings.BASE_DIR / f'data/modality.csv', 'r', encoding='utf-8'
                ) as f:
            reader = csv.reader(f)
            next(reader)  # Пропустить строку заголовка.
            for row in reader:
                specialization = Specialization.objects.get(code=row[1])
                modality, created = Modality.objects.get_or_create(
                    modality=row[0],
                    modality_specialization=specialization
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{_('Успешно добавлено') if created else _('Уже существует')}: {row[0]} - {row[1]}"
                    )
                )
        with open(
            settings.BASE_DIR / f'data/examination_modality.csv', 'r', encoding='utf-8'
                ) as f:
            reader = csv.reader(f)
            next(reader)  # Пропустить строку заголовка.
            for row in reader:
                modality = Modality.objects.get(modality=row[0])
                examination, created = MedicalExamination.objects.get_or_create(
                    code=int(row[1]),
                    examination_modality=modality,
                    examination_type=row[2],
                    conventional_units=float(row[3])
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{_('Успешно добавлено') if created else _('Уже существует')}: {row[0]} - {row[1]} - {row[2]} - {row[3]}"
                    )
                )            
