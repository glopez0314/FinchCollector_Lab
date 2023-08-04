# Generated by Django 4.2.3 on 2023-08-03 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0003_alter_dog_breed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Playdate",
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
                ("date", models.DateTimeField(verbose_name="Schedule Play Date")),
                (
                    "length",
                    models.IntegerField(max_length=1, verbose_name="How many hours"),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Your Name")),
                (
                    "dog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main_app.dog"
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
