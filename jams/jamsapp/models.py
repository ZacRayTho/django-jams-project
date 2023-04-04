from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=55)
    publish_date = models.DateField()
    cover_art = models.URLField(null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
        
class Artist(models.Model):
    name = models.CharField(max_length=55)
    bio = models.TextField(null=False)
    image = models.URLField(null=False)


    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=55)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    genres = models.ManyToManyField(Genre)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=55)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
