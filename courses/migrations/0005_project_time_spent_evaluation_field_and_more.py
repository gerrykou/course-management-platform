# Generated by Django 4.2.9 on 2024-01-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_project_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="time_spent_evaluation_field",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="project",
            name="time_spent_project_field",
            field=models.BooleanField(default=True),
        ),
    ]
