# Generated by Django 4.2.1 on 2023-05-10 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_tracker', '0003_alter_player_team'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='team',
            unique_together={('city', 'mascot')},
        ),
    ]
