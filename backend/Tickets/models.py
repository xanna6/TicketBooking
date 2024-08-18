import base64
from datetime import datetime

from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_path = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Hall(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    rows = models.IntegerField(blank=True, null=True)
    seats_in_row = models.IntegerField(blank=True, null=True)


class Screening(models.Model):
    id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
