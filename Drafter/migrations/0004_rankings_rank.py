# Generated by Django 4.1.4 on 2022-12-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drafter', '0003_remove_rankings_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='rankings',
            name='rank',
            field=models.IntegerField(max_length=15, null=True, verbose_name='RK'),
        ),
    ]
