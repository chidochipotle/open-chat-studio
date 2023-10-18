# Generated by Django 4.2 on 2023-10-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0041_default_consent_and_add_users_to_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="syntheticvoice",
            name="language_code",
            field=models.CharField(
                default="<undef>", help_text="The language code this voice is for", max_length=32
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="syntheticvoice",
            name="service",
            field=models.CharField(
                choices=[("AWS", "AWS"), ("Azure", "Azure")],
                default="AWS",
                help_text="The service this voice is from",
                max_length=6,
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="syntheticvoice",
            unique_together={("name", "language_code", "language", "gender", "neural", "service")},
        ),
    ]