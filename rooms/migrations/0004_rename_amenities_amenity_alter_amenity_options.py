# Generated by Django 4.1.7 on 2023-03-06 15:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0003_rename_amenity_amenities_alter_amenities_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Amenities",
            new_name="Amenity",
        ),
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
    ]
