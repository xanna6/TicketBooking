from datetime import date, datetime

import pytz
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from Tickets.models import User, Movie, Screening, Ticket, Customer
from Tickets.serializers import UserSerializer, MovieSerializer, ScreeningSerializer, TicketSerializer, \
    CustomerSerializer


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
                date=filter_date,
                time__gt=current_time
            )
        else:
            screenings = Screening.objects.filter(
                date=filter_date
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
                date=filter_date,
                time__gt=current_time
            )
        else:
            screenings = Screening.objects.filter(
                movie=movie,
                date=filter_date
            )

        serializer = MovieSerializer(movie, context={'request': request})
        data = serializer.data
        data['screenings'] = ScreeningSerializer(screenings, many=True).data

        return Response(data)


class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        screening_id = self.request.query_params.get('screening_id')

        try:
            screening = Screening.objects.get(id=screening_id)
        except Screening.DoesNotExist:
            raise ValidationError({"screening": "Screening not found."})

        data = request.data
        data['screening'] = screening.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['patch'], url_path='submit')
    def patch_multiple(self, request):
        data = request.data
        ticketIds = data.get('ids')

        try:
            with transaction.atomic():
                for ticketId in ticketIds:
                    ticket = Ticket.objects.get(pk=ticketId)
                    ticket_new_data = {
                        "customer": data.get('customer_id'),
                        "sold": True,
                        "sold_timestamp": datetime.now().isoformat()
                    }
                    serializer = self.get_serializer(ticket, data=ticket_new_data, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
        except Ticket.DoesNotExist as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Tickets updated successfully."}, status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
