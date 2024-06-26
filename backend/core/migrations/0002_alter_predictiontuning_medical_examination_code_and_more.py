# Generated by Django 5.0.6 on 2024-06-11 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
        (
            "medical_examination",
            "0005_remove_medicalexamination_id_medicalexamination_code",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictiontuning",
            name="medical_examination_code",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="medical_examination.medicalexamination",
            ),
        ),
        migrations.AlterField(
            model_name="predictiontuning",
            name="seasonality",
            field=models.CharField(
                choices=[
                    (
                        "daily",
                        "Ежедневная сезонность, рекомендовано period=1, fourier_order=3",
                    ),
                    (
                        "weekly",
                        "Еженедельная сезонность, рекомендовано period=7, fourier_order=3",
                    ),
                    (
                        "monthly",
                        "Ежемесячная сезонность, рекомендовано period=30.5, fourier_order=5",
                    ),
                    (
                        "yearly",
                        "Годовая сезонность, рекомендовано period=365, fourier_order=10",
                    ),
                ],
                default="weekly",
                max_length=20,
            ),
        ),
    ]
