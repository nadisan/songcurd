from django.db import models
from django.utils import timezone

# Create your models here.

   
class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age=models.IntegerField(default='null')
	
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=400)
    date_released = models.DateField(help_text="year-month-date", null=True)
    likes = models.CharField(max_length=400)
    artiste_id = models.CharField(max_length=40,null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} : sung by  {self.Artiste}'
	
	

class Lyric(models.Model):
    Artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE,null=True)
    Song = models.ForeignKey(Song,on_delete=models.CASCADE,null=True)
    content = models.TextField(max_length=1000, help_text="Enter Lyric's of the song")
    song_id = models.CharField(max_length=40,null=True, blank=True)
    
    def __str__(self):
        if len(self.content) > 10:
            return f"{self.content[0:10]}...song title: {self.Song.title}"
        else:
            return f"{self.content} ...song title: {self.Song.title}"