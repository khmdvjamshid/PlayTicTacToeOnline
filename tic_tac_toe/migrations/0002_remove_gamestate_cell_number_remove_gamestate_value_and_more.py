# Generated by Django 4.2.1 on 2023-05-25 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("tic_tac_toe", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="gamestate", name="cell_number",),
        migrations.RemoveField(model_name="gamestate", name="value",),
        migrations.AddField(
            model_name="gamestate",
            name="state",
            field=models.CharField(default=django.utils.timezone.now, max_length=9),
            preserve_default=False,
        ),
    ]
