# Generated by Django 4.1.2 on 2022-11-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_remove_lyric_songid'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
