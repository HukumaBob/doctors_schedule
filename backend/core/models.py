from django.db import models
from django.utils.translation import gettext_lazy as _

from medical_examination.models import MedicalExamination

# Тонкая настройка предсказаний
class PredictionTuning(models.Model):
    medical_examination_code = models.OneToOneField(
        MedicalExamination,
        on_delete=models.CASCADE,
        )
    # модель роста
    GROWTH_CHOICES = [
        ('linear', _('Линейная модель роста')),
        ('logistic', _('Логистическая модель роста')),
    ]    
    growth = models.CharField(
        max_length=20, 
        choices=GROWTH_CHOICES,
        default='logistic',
        )
    # предел насыщения для каждого периода времени
    cap = models.FloatField(default=200)
    floor = models.FloatField(default=0)
    # сезонность
    SEASONALITY_CHOICES = [
        ('daily', _(
            'Ежедневная сезонность, рекомендовано period=1, fourier_order=3'
            )),
        ('weekly', _(
            'Еженедельная сезонность, рекомендовано period=7, fourier_order=3'
            )),
        ('monthly', _(
            'Ежемесячная сезонность, рекомендовано period=30.5, fourier_order=5'
            )),       
        ('yearly', _(
            'Годовая сезонность, рекомендовано period=365, fourier_order=10'
            )),                          
    ]        
    seasonality = models.CharField(
        max_length=20, 
        choices=SEASONALITY_CHOICES,
        default='weekly'
        )
    seasonality_period = models.FloatField(default=7)
    seasonality_fourier_order = models.IntegerField(default=3)
    # сила сезонности, чем больше, тем гибче
    seasonality_prior_scale = models.FloatField(default=0.02)
