# Generated by Django 4.2.1 on 2023-05-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "tic_tac_toe",
            "0002_remove_gamestate_cell_number_remove_gamestate_value_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="WinState",
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
                ("symbol", models.CharField(max_length=1)),
            ],
        ),
    ]
