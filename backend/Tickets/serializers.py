from datetime import date, datetime

import pytz
from rest_framework import serializers

from Tickets.models import User, Movie, Hall, HallScreeningTime, Screening


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class HallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'name', 'rows', 'seats_in_row']


class HallScreeningTimeSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format='%H:%M')
    hall = HallSerializer()

    class Meta:
        model = HallScreeningTime
        fields = ['id', 'date', 'time', 'hall']


class ScreeningSerializer(serializers.ModelSerializer):
    hall_screening_time = HallScreeningTimeSerializer()

    class Meta:
        model = Screening
        fields = ['id', 'hall_screening_time']


def get_local_time():
    local_tz = pytz.timezone('Europe/Warsaw')
    return datetime.now(local_tz).time()


class MovieSerializer(serializers.ModelSerializer):
    screenings = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image_path', 'date_added', 'screenings']

    def get_screenings(self, obj):
        request = self.context.get('request')
        date_param = request.query_params.get('date')
        current_date = datetime.now().date()
        current_time = get_local_time()

        if date_param:
            filter_date = date.fromisoformat(date_param)
        else:
            filter_date = current_date

        if filter_date == current_date:
            screenings = Screening.objects.filter(
                movie=obj,
                hall_screening_time__date=filter_date,
                hall_screening_time__time__gt=current_time
            )
        else:
            screenings = Screening.objects.filter(
                movie=obj,
                hall_screening_time__date=filter_date
            )

        return ScreeningSerializer(screenings, many=True).data
