from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from faker import Faker
from users.models import User, UserProfile, Specialization, Modality, UserProfileModality
import random

class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **options):
        fake = Faker()
        for us in range(100):  # создаем 100 фейковых юзеров
            user, created = User.objects.get_or_create(username=fake.name(), password='12345678')
            self.stdout.write(
                self.style.SUCCESS(
                    f"{_('Успешно добавлено') if created else _('Уже существует')}: {user.username}"
                )
            )
        
        users = User.objects.all()
        specializations = Specialization.objects.all()
        modalities = Modality.objects.all()

        for user in users:
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                phone=fake.phone_number(),
                place_of_work="Mayo Clinic",
                position='doctor',
                specialization=fake.random.choice(specializations),
                wage_rate=fake.random.choice([0.25, 0.5, 0.75, 1.0, 1.25]),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"{_('Успешно добавлено') if created else _('Уже существует')}: {profile}"
                )
            )
            user_profile = UserProfile.objects.get(user=user)
            modalities_list = list(modalities)
            random.shuffle(modalities_list)  # перемешиваем список модальностей
            for i, modality in enumerate(modalities_list):
                UserProfileModality.objects.create(
                    user_profile=user_profile,
                    modality=modality,
                    priority=(i == 0)  # только первая модальность будет иметь приоритет
                )
