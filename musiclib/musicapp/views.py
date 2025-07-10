from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Albhum, Song
from .serializers import AlbhumSerializer, SongSerializer
from django.shortcuts import render

#Albhum CRUD operations

@api_view(['POST'])
def create_albhum(request):
    serializer = AlbhumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Albhum created successfull"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_albhum(request):
    albhums = Albhum.objects.all()
    serializer = AlbhumSerializer(albhums, many=True)
    if albhums.exists():
        return Response({"albhums" : serializer.data})
    return Response({"message" : "empty list"})

@api_view(['GET'])
def get_album(request, pk):
    try:
        album = Albhum.objects.get(pk=pk)
    except Albhum.DoesNotExist:
        return Response({'error': 'Album not found'}, status=404)
    serializer = AlbhumSerializer(album)
    return Response(serializer.data)

@api_view(['PUT'])
def update_album(request, pk):
    try:
        album = Albhum.objects.get(pk=pk)
    except Albhum.DoesNotExist:
        return Response({'error': 'Album not found'}, status=404)
    serializer = AlbhumSerializer(album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_album(request, pk):
    try:
        album = Albhum.objects.get(pk=pk)
        album.delete()
        return Response({'message': 'Album deleted'}, status=204)
    except Albhum.DoesNotExist:
        return Response({'error': 'Album not found'}, status=404)

#Song CRUD operations

@api_view(['POST'])
def create_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "song created successful", "song": serializer.data}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response({"songs" : serializer.data})
@api_view(['GET'])
def get_song(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song not found'}, status=404)
    serializer = SongSerializer(song)
    return Response(serializer.data)

@api_view(['PUT'])
def update_song(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song not found'}, status=404)
    serializer = SongSerializer(song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_song(request, pk):
    try:
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response({'message': 'Song deleted'}, status=204)
    except Song.DoesNotExist:
        return Response({'error': 'Song not found'}, status=404)




