# Generated by Django 4.1.7 on 2023-03-06 16:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Experiencee",
            new_name="Experience",
        ),
    ]
