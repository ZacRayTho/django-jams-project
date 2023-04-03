from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=55)
    bio = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name
# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=55)
    publish_date = models.DateField()
    cover_art = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
        
class Song(models.Model):
    name = models.CharField(max_length=55)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name