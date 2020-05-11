from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request,artist_id):
    artists = Artist.objects.get(id=artist_id)
    serializer = ArtistSerializer(artists)

    return Response(serializer.data)