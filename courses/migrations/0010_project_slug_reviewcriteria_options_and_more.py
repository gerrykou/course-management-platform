# Generated by Django 4.2.9 on 2024-01-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "courses",
            "0009_project_reviewcriteria_projectsubmission_peerreview_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="slug",
            field=models.SlugField(default="fake-course"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reviewcriteria",
            name="options",
            field=models.JSONField(default="fake-course"),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="project",
            unique_together={("course", "slug")},
        ),
    ]
