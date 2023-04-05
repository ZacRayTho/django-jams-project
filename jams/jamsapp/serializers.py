from django.contrib.auth.models import User, Group
from rest_framework import serializers
from jamsapp.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    song = serializers.StringRelatedField(many=True)
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image', 'song']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    song = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['name', 'publish_date', 'cover_art', 'song']

class AlbumEditSerializer(serializers.HyperlinkedModelSerializer):
    song = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)

    class Meta:
        model = Album
        fields = ['name', 'publish_date', 'cover_art', 'song']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class SongSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.StringRelatedField()
    artist = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Song
        fields = ['name', 'duration', 'album', 'genres', 'artist']

class SongEditSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), many=True)
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Song
        fields = ['name', 'duration', 'album', 'genres', 'artist']

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Playlist
        fields = ['name', 'songs']

class PlaylistEditSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)

    class Meta:
        model = Playlist
        fields = ['name', 'songs']