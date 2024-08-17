from datetime import date, datetime

import pytz
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from Tickets.models import User, Movie, Screening
from Tickets.serializers import UserSerializer, MovieSerializer, ScreeningSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


def get_local_time():
    local_tz = pytz.timezone('Europe/Warsaw')
    return datetime.now(local_tz).time()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        date_param = self.request.query_params.get('date')
        title_param = self.request.query_params.get('title')
        current_date = datetime.now().date()
        current_time = get_local_time()

        if title_param:
            queryset = queryset.filter(title__icontains=title_param)

        if date_param:
            filter_date = date.fromisoformat(date_param)
        else:
            filter_date = current_date

        if filter_date == current_date:
            screenings = Screening.objects.filter(
                hall_screening_time__date=filter_date,
                hall_screening_time__time__gt=current_time
            )
        else:
            screenings = Screening.objects.filter(
                hall_screening_time__date=filter_date
            )

        movie_ids = screenings.values_list('movie_id', flat=True)
        queryset = queryset.filter(id__in=movie_ids)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MovieDetailsViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        date_param = self.request.query_params.get('date')
        current_date = datetime.now().date()
        current_time = get_local_time()
        filter_date = date.fromisoformat(date_param)

        movie = get_object_or_404(Movie, pk=kwargs['pk'])

        if filter_date == current_date:
            screenings = Screening.objects.filter(
                movie=movie,
                hall_screening_time__date=filter_date,
                hall_screening_time__time__gt=current_time
            )
        else:
            screenings = Screening.objects.filter(
                movie=movie,
                hall_screening_time__date=filter_date
            )

        serializer = MovieSerializer(movie, context={'request': request})
        data = serializer.data
        data['screenings'] = ScreeningSerializer(screenings, many=True).data

        return Response(data)


class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
