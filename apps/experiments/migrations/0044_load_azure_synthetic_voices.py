# Generated by Django 4.2 on 2023-10-11 15:32
import os
import json
from django.db import migrations

def load_azure_synthetic_voices(apps, schema_editor):
    SyntheticVoice = apps.get_model("experiments", "SyntheticVoice")
    voice_data = {}
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "preload_data/azure_voices.json")

    with open(file_path, "r") as json_file:
        voice_data = json.load(json_file)["voices"]

    voices_created = 0
    for voice in voice_data:
        _, created = SyntheticVoice.objects.get_or_create(
            name=voice["name"],
            language=voice["language"],
            language_code=voice["language_code"],
            gender=voice["gender"],
            neural=voice["neural"],
            service="Azure",
        )

        if created:
            voices_created += 1
    print(f"{voices_created} synthetic voices were created")

def drop_synthetic_voices(apps, schema_editor):
    SyntheticVoice = apps.get_model("experiments", "SyntheticVoice")
    SyntheticVoice.objects.filter(service="Azure").delete()

class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0043_update_AWS_synthetic_voices"),
    ]

    operations = [migrations.RunPython(load_azure_synthetic_voices, drop_synthetic_voices)]