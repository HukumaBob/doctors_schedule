from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from medical_examination.models import Modality
from production_calendar.models import OperatingMode


class User(AbstractUser):
    user_photo = models.ImageField(
        verbose_name=_("Фото"),
        upload_to='images/',
        blank=True, null=True,
    )    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('Группы'),
        blank=True,
        help_text=_(
            'Группы, к которым принадлежит этот пользователь. '
            'Пользователь получит все разрешения '
            'предоставлено каждой из их групп.'
        ),
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('Разрешения для юзера'),
        blank=True,
        help_text=_('Специальные разрешения для этого юзера.'),
        related_name="custom_user_set",
        related_query_name="user",
    )
 

class Specialization(models.Model):
    code = models.IntegerField(primary_key=True)
    specialization = models.CharField(max_length=100)    
    def __str__(self):
        return self.specialization    

class UserProfile(models.Model):
    POSITION_CHOICES = [
        ('ceo', _('Руководитель')),
        ('hr', _('Кадровик')),
        ('doctor', _('Врач')),
    ]
    WAGE_CHOICES = [
        (0.25, '0.25'),
        (0.5, '0.5'),
        (0.75, '0.75'),
        (1.0, '1.0'),
        (1.25, '1.25'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    place_of_work = models.CharField(max_length=255)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    modality = models.ManyToManyField(Modality, through='UserProfileModality')
    wage_rate = models.DecimalField(
        max_digits=3, decimal_places=2, choices=WAGE_CHOICES, default=1
        )
    operating_mode = models.ForeignKey(OperatingMode, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.position} {self.user}'

class UserProfileModality(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    priority = models.BooleanField(default=False, null=True)
    class Meta:
        unique_together = ('user_profile', 'modality')

# Тут надо добавить обработчик исключений для DRF
@receiver(pre_save, sender=UserProfileModality)
def validate_priority(sender, instance, **kwargs):
    if instance.priority:
        has_priority = UserProfileModality.objects.filter(
            user_profile=instance.user_profile,
            priority=True
        ).exists()
        if has_priority:
            raise ValidationError('Priority for this user already exists.')
