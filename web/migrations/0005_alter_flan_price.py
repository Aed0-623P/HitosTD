# Generated by Django 4.2 on 2024-04-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_flan_price_delete_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flan",
            name="price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]