# Generated by Django 4.2.14 on 2024-11-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emran", "0007_publications_pub_serial_no"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacts",
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
                ("con_loc", models.CharField(max_length=300)),
                ("con_email", models.CharField(blank=True, max_length=300, null=True)),
                ("con_skype", models.CharField(blank=True, max_length=500, null=True)),
                ("con_phone", models.CharField(blank=True, max_length=100, null=True)),
                ("con_map_link", models.CharField(max_length=500)),
            ],
        ),
    ]
