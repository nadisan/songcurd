# Generated by Django 4.1.2 on 2022-10-30 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_rename_artist_id_song_artist_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='Song_id',
            new_name='Songid',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='Artist_Id',
            new_name='artistid',
        ),
    ]