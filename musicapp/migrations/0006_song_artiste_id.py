# Generated by Django 4.1.2 on 2022-11-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_remove_song_artiste_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
