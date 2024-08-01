import base64

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


class HallScreeningTime(models.Model):
    id = models.IntegerField(primary_key=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


class Screening(models.Model):
    id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_screening_time = models.ForeignKey(HallScreeningTime, on_delete=models.CASCADE)
