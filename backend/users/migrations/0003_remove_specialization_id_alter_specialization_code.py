# Generated by Django 5.0.6 on 2024-06-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_specialization_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialization',
            name='id',
        ),
        migrations.AlterField(
            model_name='specialization',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
