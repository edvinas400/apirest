# Generated by Django 4.1.6 on 2023-02-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0002_alter_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='Song duration in seconds'),
        ),
    ]