# Generated by Django 5.0.6 on 2024-06-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorschedule',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctorschedule',
            name='lunch_break',
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
    ]
