# Generated by Django 4.1.2 on 2022-11-04 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_rename_song_id_lyric_songid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='songid',
        ),
    ]
