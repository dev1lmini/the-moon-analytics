# Generated by Django 3.1.8 on 2021-10-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0176_update_person_props_function"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="path_cleaning_filters",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
