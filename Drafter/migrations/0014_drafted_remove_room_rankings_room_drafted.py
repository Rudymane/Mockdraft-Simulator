# Generated by Django 4.0.1 on 2022-12-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drafter', '0013_alter_rankings_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drafted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='rankings',
        ),
        migrations.AddField(
            model_name='room',
            name='drafted',
            field=models.ManyToManyField(related_name='drafted', to='Drafter.Drafted'),
        ),
    ]
