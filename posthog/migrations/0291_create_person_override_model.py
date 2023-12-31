# Generated by Django 3.2.16 on 2023-01-19 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0290_add_dashboard_templates"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonOverride",
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
                ("old_person_id", models.UUIDField(db_index=True)),
                ("override_person_id", models.UUIDField(db_index=True)),
                ("oldest_event", models.DateTimeField()),
                ("version", models.BigIntegerField(blank=True, null=True)),
                (
                    "team",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.team"),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="personoverride",
            constraint=models.UniqueConstraint(
                fields=("team", "old_person_id"),
                name="unique override per old_person_id",
            ),
        ),
    ]
