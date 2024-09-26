from datetime import datetime, timedelta

import pytz
from django.core.management import BaseCommand
from django.db import transaction

from Tickets.models import Movie, Screening, Hall, Customer, Ticket


def insert_hall_data():
    halls = [
        {'name': 'Mars', 'rows': 5, 'seats_in_row': 10},
        {'name': 'Jupiter', 'rows': 8, 'seats_in_row': 12},
        {'name': 'Saturn', 'rows': 8, 'seats_in_row': 15},
        {'name': 'Neptune', 'rows': 10, 'seats_in_row': 10},
    ]

    for hall_data in halls:
        Hall.objects.create(**hall_data)


def insert_movie_data():
    movies = [
        {'title': 'The Avengers', 'description': '', 'image_path': 'uploads/avengers.jpg'},
        {'title': 'The Notebook', 'description': '', 'image_path': 'uploads/notebook.jpg'},
        {'title': 'Iron Man', 'description': 'After being held captive in an Afghan cave, billionaire engineer '
                                             'Tony Stark creates a unique weaponized suit of armor to fight '
                                             'evil.', 'image_path': 'uploads/ironman.jpg'},
        {'title': 'Iron Man 2', 'description': 'World now aware of his identity as Iron Man, Tony Stark must '
                                               'contend with both his declining health and a vengeful mad man '
                                               'with ties to his father\'s legacy.',
         'image_path': 'uploads/ironman2.jpg'},
    ]

    for movie_data in movies:
        Movie.objects.create(**movie_data)


def insert_screening_data():
    today = datetime.now().date()
    hall_list = Hall.objects.all()
    for movie in Movie.objects.all():
        for i in range(5):
            screening_date = today + timedelta(days=i)
            for j in range(4):
                screening_datetime = datetime.combine(screening_date, datetime.min.time()).replace(hour=9 + 3 * j)
                Screening.objects.create(movie=movie, date=screening_date, time=screening_datetime.time(),
                                         hall=hall_list[j])


def insert_customer_data():
    customers = [
        {'firstname': 'John', 'lastname': 'Smith', 'email': 'john@mail.com', 'phone': '123456789'},
        {'firstname': 'John', 'lastname': 'Black', 'email': 'john@mail.com', 'phone': '987654321'},
    ]

    for customer_data in customers:
        Customer.objects.create(**customer_data)


def insert_ticket_data():
    customer = Customer.objects.first()
    for screening in Screening.objects.all():
        for i in range(3):
            for j in range(6):
                Ticket.objects.create(screening=screening, customer=customer, row=i, seat_in_row=j,
                                      booked=True,
                                      booked_timestamp=pytz.timezone('Europe/Warsaw').localize(datetime.now()),
                                      sold=True,
                                      sold_timestamp=pytz.timezone('Europe/Warsaw').localize(datetime.now()))


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **kwargs):

        Ticket.objects.all().delete()
        Screening.objects.all().delete()
        Movie.objects.all().delete()
        Customer.objects.all().delete()
        Hall.objects.all().delete()

        try:
            with transaction.atomic():
                insert_hall_data()
                insert_movie_data()
                insert_screening_data()
                insert_customer_data()
                insert_ticket_data()
                self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR("An error occurred while writing data to the database. Sample data has "
                                               "not been created. Error: " + str(e)))
