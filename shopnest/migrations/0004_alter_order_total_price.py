# Generated by Django 4.2.2 on 2023-10-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopnest", "0003_order_order_number_order_order_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
