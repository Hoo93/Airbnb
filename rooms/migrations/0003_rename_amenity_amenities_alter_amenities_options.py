# Generated by Django 4.1.7 on 2023-03-06 15:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_room_name_alter_amenity_description"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Amenity",
            new_name="Amenities",
        ),
        migrations.AlterModelOptions(
            name="amenities",
            options={"verbose_name_plural": "Amenity"},
        ),
    ]
