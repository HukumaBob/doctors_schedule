# Generated by Django 5.0.6 on 2024-06-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_examination', '0004_modality_modality_specialization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalexamination',
            name='id',
        ),
        migrations.AddField(
            model_name='medicalexamination',
            name='code',
            field=models.IntegerField(default=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]