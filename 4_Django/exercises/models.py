from django.db import models

GENRE = (
    (-1, 'fasdfasdfasd'),
    (0, 'POP' ),
    (1, 'rock')
)
# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRE, default=-1)

    def __str__(self):
        return self.name+" "+ str(self.year)
RATING = (
    (1,'BAD'),
    (2,'NOT SO BAD'),
    (3,'EEE'),
    (4,'GOOD'),
    (5,'VERY GOOOOOD'),
)
class Album(models.Model):
    title = models.CharField(max_length=124)
    year = models.IntegerField()
    rating = models.IntegerField(choices=RATING)
    band = models.ForeignKey(Band, on_delete=models.DO_NOTHING)


album_rating=(
    (0,"one"),
    (1,'two'),
    (2, 'smash'),
    (3, 'overwatch'),
    (4, '')
)

