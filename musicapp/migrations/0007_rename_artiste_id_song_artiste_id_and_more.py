# Generated by Django 4.1.2 on 2022-11-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0006_song_artiste_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artiste_id',
            new_name='Artiste_id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='Artiste',
        ),
    ]