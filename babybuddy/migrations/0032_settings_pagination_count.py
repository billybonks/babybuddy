# Generated by Django 5.0.6 on 2024-05-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("babybuddy", "0031_alter_settings_timezone"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="pagination_count",
            field=models.PositiveIntegerField(
                choices=[
                    (10, "10 Per Page"),
                    (25, "25 Per Page"),
                    (50, "50 Per Page"),
                    (100, "100 Per Page"),
                ],
                default=25,
                verbose_name="Items Per Page",
            ),
        ),
    ]
