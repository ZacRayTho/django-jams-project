from rest_framework import viewsets
from rest_framework import permissions
from jamsapp.serializers import *
from django.http import HttpResponse

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
# Create your views here.
class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer

class SongEditViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongEditSerializer
    http_method_names = ('post', 'put', 'patch', 'delete')

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


def genre_list(request):
    genres = Genre.objects.all()
    html = ''
    for genre in genres:
        html += '<li>%s</li>'% genre
    return HttpResponse(html)

def song_lookup(request, song_id):
    chosen = Song.objects.get(pk=song_id)
    return HttpResponse("You Chose '%s'!"% chosen)
    