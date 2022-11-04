from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.//

def index(request):
   return HttpResponse ( 'Welcome to my Django,Artiste lists at http://127.0.0.1:8000/musicapp/Artiste, Song list at http://127.0.0.1:8000/musicapp/Song')



#def Song_list (request):
    
    #songs = Song.objects.all()
    #serializer = musicappSerializer(songs, many=True)
   # return JsonResponse(serializer.data, safe=False)