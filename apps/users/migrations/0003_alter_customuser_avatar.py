# Generated by Django 4.2.7 on 2023-12-11 08:32

import apps.web.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.FileField(
                blank=True, storage=apps.web.storage_backends.get_public_media_storage, upload_to="profile-pictures/"
            ),
        ),
    ]