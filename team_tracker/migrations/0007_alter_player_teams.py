# Generated by Django 4.2.1 on 2023-05-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_tracker', '0006_alter_player_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(related_name='players', to='team_tracker.team'),
        ),
    ]
