# Generated by Django 4.2.2 on 2023-10-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopnest", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.AddField(
            model_name="product",
            name="image_url",
            field=models.URLField(null=True),
        ),
    ]
