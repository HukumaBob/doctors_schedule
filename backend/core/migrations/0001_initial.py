# Generated by Django 5.0.6 on 2024-06-11 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_examination', '0005_remove_medicalexamination_id_medicalexamination_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionTuning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('growth', models.CharField(choices=[('linear', 'Линейная модель роста'), ('logistic', 'Логистическая модель роста')], default='logistic', max_length=20)),
                ('cap', models.FloatField(default=200)),
                ('floor', models.FloatField(default=0)),
                ('seasonality', models.CharField(choices=[('daily', 'Ежедневная сезонность, рекомендовано period=1, fourier_order=3'), ('weekly', 'Еженедельная сезонность, рекомендовано period=7, fourier_order=3'), ('monthly', 'Ежемесячная сезонность, рекомендовано period=30.5, fourier_order=5'), ('yearly', 'Годовая сезонность, рекомендовано period=365, fourier_order=10')], max_length=20)),
                ('seasonality_period', models.FloatField(default=7)),
                ('seasonality_fourier_order', models.IntegerField(default=3)),
                ('seasonality_prior_scale', models.FloatField(default=0.02)),
                ('medical_examination_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_examination.medicalexamination')),
            ],
        ),
    ]
