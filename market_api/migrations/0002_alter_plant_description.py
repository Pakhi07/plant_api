# Generated by Django 4.2 on 2023-04-16 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="description",
            field=models.CharField(blank=True, default="", max_length=1000),
        ),
    ]