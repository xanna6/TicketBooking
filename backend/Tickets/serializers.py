from django.urls import reverse
from rest_framework import serializers

from Tickets.models import User, Movie, Hall, HallScreeningTime, Screening


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class HallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class HallScreeningTimeSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = HallScreeningTime
        fields = ['id', 'date', 'time']


class ScreeningSerializer(serializers.ModelSerializer):
    hall_screening_time = HallScreeningTimeSerializer()

    class Meta:
        model = Screening
        fields = ['hall_screening_time']


class MovieSerializer(serializers.ModelSerializer):
    screenings = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_path', 'date_added', 'screenings']

    def get_screenings(self, obj):
        screenings = Screening.objects.filter(movie=obj)
        return ScreeningSerializer(screenings, many=True).data
