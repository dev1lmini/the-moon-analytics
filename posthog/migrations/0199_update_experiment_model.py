# Generated by Django 3.2.5 on 2022-01-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0198_async_migration_error"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="experiment",
            name="secondary_metrics",
            field=models.JSONField(default=list, null=True),
        ),
    ]
