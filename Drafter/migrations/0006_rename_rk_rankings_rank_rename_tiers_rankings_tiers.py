# Generated by Django 4.1.4 on 2022-12-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Drafter', '0005_rename_rank_rankings_rk_rename_tiers_rankings_tiers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rankings',
            old_name='RK',
            new_name='rank',
        ),
        migrations.RenameField(
            model_name='rankings',
            old_name='TIERS',
            new_name='tiers',
        ),
    ]
