# Generated by Django 4.2.1 on 2023-06-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="Token",
            field=models.CharField(max_length=255),
        ),
    ]
