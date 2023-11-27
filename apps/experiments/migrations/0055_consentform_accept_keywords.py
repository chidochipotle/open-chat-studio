# Generated by Django 4.2.7 on 2023-11-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0054_consentform_capture_identifier_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="consentform",
            name="accept_keywords",
            field=models.CharField(
                default="yes",
                help_text="A list of words (separated by a comma) that the user should respond with to give consent",
                max_length=200,
            ),
        ),
    ]
