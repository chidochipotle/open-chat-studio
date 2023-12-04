# Generated by Django 4.2 on 2023-11-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("channels", "0012_experimentchannel_messaging_provider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experimentchannel",
            name="platform",
            field=models.CharField(
                choices=[("telegram", "Telegram"), ("web", "Web"), ("whatsapp", "WhatsApp"), ("facebook", "Facebook")],
                default="telegram",
                max_length=32,
            ),
        ),
    ]