# Generated by Django 4.2.14 on 2024-11-15 16:04

from django.db import migrations, models
import emran.models


class Migration(migrations.Migration):

    dependencies = [
        ("emran", "0003_volunteering_volunteering_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeyInformation",
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
                ("ki_type", models.CharField(max_length=300)),
                ("ki_amount", models.IntegerField()),
                ("ki_names", models.CharField(max_length=500)),
                ("ki_sort_description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="certificationscoursestrainings",
            name="cct_serial_no",
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="volunteering",
            name="volunteering_image",
            field=models.ImageField(
                blank=True,
                max_length=500,
                null=True,
                upload_to=emran.models.get_Volunteering_upload_path,
            ),
        ),
    ]
