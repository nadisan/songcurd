# Generated by Django 4.1.2 on 2022-11-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_lyric_song_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artiste_id',
        ),
    ]
