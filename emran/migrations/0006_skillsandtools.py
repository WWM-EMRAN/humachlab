# Generated by Django 4.2.14 on 2024-09-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emran", "0005_alter_honorsandawards_haw_associated_organisation"),
    ]

    operations = [
        migrations.CreateModel(
            name="SkillsAndTools",
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
                ("sat_title", models.CharField(max_length=300)),
                ("sat_short_description", models.CharField(max_length=600)),
                ("sat_description", models.TextField(blank=True, null=True)),
                ("sat_skill_level", models.IntegerField()),
            ],
        ),
    ]