# Generated by Django 4.2 on 2023-04-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamsapp', '0005_remove_artist_songs_song_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(related_name='artist', to='jamsapp.artist'),
        ),
    ]
