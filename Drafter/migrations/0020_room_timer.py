# Generated by Django 4.0.1 on 2023-01-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drafter', '0019_room_user_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='timer',
            field=models.IntegerField(default=15),
        ),
    ]
