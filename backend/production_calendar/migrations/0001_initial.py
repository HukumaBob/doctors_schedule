# Generated by Django 5.0.6 on 2024-06-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('day_type', models.CharField(choices=[('workday', 'Рабочий'), ('day_off', 'Выходной'), ('holiday', 'Праздничный'), ('pre_holiday', 'Предпраздничный')], max_length=20)),
                ('work_hours', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
