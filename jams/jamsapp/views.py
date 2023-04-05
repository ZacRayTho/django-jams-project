from rest_framework import viewsets
from rest_framework import permissions
from jamsapp.serializers import *
from django.http import HttpResponse

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ArtistSerializer
        else:
            return ArtistEditSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AlbumSerializer
        else:
            return AlbumEditSerializer
# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SongSerializer
        else:
            return SongEditSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PlaylistSerializer
        else:
            return PlaylistEditSerializer


def genre_list(request):
    genres = Genre.objects.all()
    html = ''
    for genre in genres:
        html += '<li>%s</li>'% genre
    return HttpResponse(html)

def song_lookup(request, song_id):
    chosen = Song.objects.get(pk=song_id)
    return HttpResponse("You Chose '%s'!"% chosen)
    