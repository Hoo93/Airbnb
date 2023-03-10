# Generated by Django 4.1.7 on 2023-03-07 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("experiences", "0003_experience_category_alter_perk_details_and_more"),
        ("rooms", "0006_room_category"),
        ("wishlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rooms.room",
            ),
        ),
    ]
