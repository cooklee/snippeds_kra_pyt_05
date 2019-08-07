from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='dirctor')
    screenplay = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='screen_play')
    starring = models.ManyToManyField(Person, related_name='actor', through='PersonMovie')
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre)

class PersonMovie(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=128)