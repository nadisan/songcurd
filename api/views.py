from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from musicapp.models import Artiste, Song, Lyric
from musicapp import models
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api import serializers

def index(request):
   return HttpResponse ('Welcome to my Django, Artiste list at http://127.0.0.1:8000/musicapp/Artiste, Song list at http://127.0.0.1:8000/musicapp/Song ')

@api_view(['GET', 'POST'])
def Artiste_list (request, format=None):
    
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
@api_view(['GET', 'POST'])
def Song_list (request, format=None):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def Lyric_list (request, format=None):
    if request.method == 'GET':
        lyrics = Lyric.objects.all()
        serializer = LyricSerializer(lyrics, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        LyricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Artiste_detail(request,id, format=None):
   
    try:
        artiste = Artiste.objects.get(pk=id)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArtisteSerializer(artiste)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET','PUT','DELETE'])
def Song_detail(request,id, format=None):
   
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def Lyric_detail(request,id, format=None):
   
    try:
        lyric = Lyric.objects.get(pk=id)
    except Lyric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LyricSerializer(lyric)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LyricSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lyric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)