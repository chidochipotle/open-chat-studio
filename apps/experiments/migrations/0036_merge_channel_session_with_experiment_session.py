# Generated by Django 4.2 on 2023-10-11 07:42

from django.db import migrations
BATCH_SIZE = 100

def update_experiment_sessions(apps, schema_editor):
    ChannelSession = apps.get_model("channels", "ChannelSession")
    ExperimentSession = apps.get_model("experiments", "ExperimentSession")
    records_updated = 0

    while True:
        channel_sessions = ChannelSession.objects.all()[records_updated:records_updated+BATCH_SIZE]
        if not channel_sessions:
            break

        dirty_experiment_sessions = []
        for channel_session in channel_sessions:
            experiment_session = channel_session.experiment_session
            experiment_session.external_chat_id = channel_session.external_chat_id
            experiment_session.experiment_channel = channel_session.experiment_channel
            dirty_experiment_sessions.append(experiment_session)
        
        ExperimentSession.objects.bulk_update(dirty_experiment_sessions, ["external_chat_id", "experiment_channel"])
        records_updated += len(channel_sessions)


def revert_update(apps, schema_editor):
    ExperimentSession = apps.get_model("experiments", "ExperimentSession")
    ExperimentSession.objects.all().update(external_chat_id=None, experiment_channel=None)

class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0035_experimentsession_experiment_channel_and_more"),
    ]

    operations = [migrations.RunPython(update_experiment_sessions, revert_update)]