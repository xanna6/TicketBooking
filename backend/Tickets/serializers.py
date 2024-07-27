from django.urls import reverse
from rest_framework import serializers

from Tickets.models import User, Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'image_path',
        ]

