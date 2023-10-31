# Generated by Django 4.2 on 2023-10-24 12:01

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("teams", "0003_flag"),
    ]

    operations = [
        migrations.CreateModel(
            name="LlmProvider",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("type", models.CharField(choices=[("openai", "OpenAI"), ("azure", "Azure OpenAI")], max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("config", django_cryptography.fields.encrypt(models.JSONField(default=dict))),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="teams.team", verbose_name="Team"
                    ),
                ),
            ],
            options={
                "ordering": ("type", "name"),
            },
        ),
    ]