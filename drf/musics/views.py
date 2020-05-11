from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse


# Create your views here.

@api_view(['GET', 'POST']) # api하는 친구를 통해 view를 생성해준다.DRF가 가지고 있는 기능. 예쁜 페이지가 나오는 이유!
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def artist_detail(request,artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        artist = Artist.objects.get(id=artist_id)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        artist = Artist.objects.get(id=artist_id)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        artist = Artist.objects.get(id=artist_id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)