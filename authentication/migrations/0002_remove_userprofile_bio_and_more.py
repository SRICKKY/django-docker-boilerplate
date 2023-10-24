# Generated by Django 4.2.2 on 2023-10-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopnest", "0002_remove_product_image_product_image_url"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="bio",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="communication_preferences",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="notifications",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="order_history",
            field=models.ManyToManyField(blank=True, to="shopnest.order"),
        ),
    ]
