# Generated by Django 4.2.7 on 2024-03-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("channels", "0014_remove_experimentchannel_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experimentchannel",
            name="name",
            field=models.CharField(
                help_text="The name of this channel", max_length=255
            ),
        ),
    ]