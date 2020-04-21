from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('artist', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Book(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} from {self.album}'
