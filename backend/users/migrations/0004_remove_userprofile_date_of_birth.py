# Generated by Django 5.0.6 on 2024-06-07 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_specialization_id_alter_specialization_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
    ]
