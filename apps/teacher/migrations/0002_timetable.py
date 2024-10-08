# Generated by Django 5.0.7 on 2024-09-25 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parent", "0003_rename_parent_id_leave_parent_and_more"),
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeTable",
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
                ("timetable_content", models.JSONField()),
                (
                    "class_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="parent.class"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="teacher.teacher",
                    ),
                ),
            ],
        ),
    ]
