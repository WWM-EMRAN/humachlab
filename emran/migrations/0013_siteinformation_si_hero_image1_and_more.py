# Generated by Django 4.2.14 on 2024-12-19 08:27

from django.db import migrations, models
import emran.models


class Migration(migrations.Migration):

    dependencies = [
        ("emran", "0012_rename_si_copyright_siteinformation_si_cr_copyright_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteinformation",
            name="si_hero_image1",
            field=models.ImageField(
                blank=True,
                max_length=500,
                null=True,
                upload_to=emran.models.get_SiteInformation_HeroBG_upload_path,
            ),
        ),
        migrations.AddField(
            model_name="siteinformation",
            name="si_hero_image2",
            field=models.ImageField(
                blank=True,
                max_length=500,
                null=True,
                upload_to=emran.models.get_SiteInformation_HeroBG_upload_path,
            ),
        ),
        migrations.AddField(
            model_name="siteinformation",
            name="si_hero_image3",
            field=models.ImageField(
                blank=True,
                max_length=500,
                null=True,
                upload_to=emran.models.get_SiteInformation_HeroBG_upload_path,
            ),
        ),
    ]
