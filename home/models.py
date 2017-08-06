from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class GameDetails(models.Model):
    game_title = models.CharField(max_length=15)
    game_icon = models.ImageField(upload_to='static/img/sports')
    page_name = models.CharField(max_length=200)
    game_intro = models.TextField(max_length=900)
    game_cover = models.ImageField(upload_to='static/img/sports')

    def __str__(self):
        return self.game_title


#class GamePage(models.Model):
    #game = models.ForeignKey(GameDetails, on_delete=models.CASCADE)
    #game_page = models.CharField(max_length=200)
    #page_name = models.CharField(max_length=200)
    #game_page = models.URLField(max_length=200)

   # def __str__(self):
        #return self.game_page


# year_choices = ('I', 'II', 'III', 'IV', 'V', 'M.tech', 'Phd')



#class PostHolderGame(models.Model):
#   ph_game = models.CharField(max_length=15)

class PostHolders(models.Model):
    ph = models.ForeignKey(GameDetails, on_delete=models.CASCADE)
    post = models.CharField(max_length=20)
    pH_name = models.CharField(max_length=20)
    game_title = models.CharField(max_length=15)
    pH_contact = models.IntegerField()
    pH_photo = models.ImageField(upload_to='static/img/postholders')

    def __str__(self):
        return self.post


class MainPostHolders(models.Model):
    post = models.CharField(max_length=20)
    pH_name = models.CharField(max_length=20)
    game_title = models.CharField(max_length=15)
    pH_contact = models.IntegerField()
    pH_photo = models.ImageField(upload_to='static/img/postholders')

    def __str__(self):
        return self.post


class GymkhanaFormModel(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    year = models.CharField(max_length=6)
    email = models.EmailField(max_length=20)
    events = models.CharField(max_length=20)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name
