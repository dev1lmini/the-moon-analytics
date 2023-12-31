# Generated by Django 3.2.5 on 2022-02-18 18:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0214_migrate_dashboard_insight_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="dashboard",
            name="tags",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                default=None,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="insight",
            name="tags",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=32),
                blank=True,
                default=None,
                null=True,
                size=None,
            ),
        ),
    ]
