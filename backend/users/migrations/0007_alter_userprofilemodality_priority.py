# Generated by Django 5.0.6 on 2024-06-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_userprofile_middle_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofilemodality",
            name="priority",
            field=models.BooleanField(default=False),
        ),
    ]
