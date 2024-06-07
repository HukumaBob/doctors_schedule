# Generated by Django 5.0.6 on 2024-06-07 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_examination', '0003_remove_modality_modality_specialization'),
        ('users', '0003_remove_specialization_id_alter_specialization_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='modality',
            name='modality_specialization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.specialization'),
            preserve_default=False,
        ),
    ]