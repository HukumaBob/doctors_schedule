# Generated by Django 5.0.6 on 2024-06-08 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_examination', '0005_remove_medicalexamination_id_medicalexamination_code'),
        ('production_calendar', '0002_operatingmode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExaminationSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_count', models.IntegerField(blank=True, null=True)),
                ('actual_count', models.IntegerField(blank=True, null=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production_calendar.calendarday')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_examination.medicalexamination')),
            ],
            options={
                'unique_together': {('day', 'examination')},
            },
        ),
    ]
