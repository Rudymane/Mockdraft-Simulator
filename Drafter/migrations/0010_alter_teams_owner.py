# Generated by Django 4.0.1 on 2022-12-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drafter', '0009_roster_teams_room_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='owner',
            field=models.CharField(default='AI', max_length=50),
        ),
    ]
