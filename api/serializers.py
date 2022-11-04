from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyric
from musicapp import models

class ArtisteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields =['first_name','last_name', 'age']

class SongSerializer (serializers.ModelSerializer):  
    class Meta:     
        model = Song
        fields =['Artiste','title','date_released','likes','artiste_id']
        read_only_fields = ['artiste_id', 'likes', 'Artiste']

class LyricSerializer (serializers.ModelSerializer):  
    class Meta:     
        model = Lyric
        fields =['content','song_id','Song']
        read_only_fields = ['song_id']


    #def get_accounts_items(self, obj):
           # Song_self = models.Artiste.objects.filter(
              #  artiste_id=obj.id)
            #serializer = ArtisteSerializer(Song_self, many=True)
    
           # return serializer.data


