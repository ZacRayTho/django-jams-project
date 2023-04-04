# Generated by Django 4.2 on 2023-04-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamsapp', '0004_rename_genre_song_genres_artist_songs_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(to='jamsapp.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_art',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(null=True),
        ),
    ]