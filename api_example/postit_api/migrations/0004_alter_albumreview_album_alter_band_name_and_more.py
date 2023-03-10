# Generated by Django 4.1.6 on 2023-02-07 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0003_alter_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='postit_api.album'),
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(max_length=150, verbose_name='band name'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='postit_api.album'),
        ),
    ]
