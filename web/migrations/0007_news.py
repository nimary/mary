# Generated by Django 4.2.1 on 2023-07-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0006_passwordresetcodes"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("text", models.TextField()),
                ("date", models.DateTimeField()),
            ],
        ),
    ]
