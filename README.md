# Ticket Booking

#### TicketBooking is a web application designed to streamline the process of reserving movie tickets. It utilizes the robust Django Rest Framework for the backend and the dynamic Vue.js for the frontend.

To run project you should have installed:

- Python
- Django
- Node.js
- PostgreSQL server


### Running backend project
Go to directory /backend:
```
cd /backend/
```

You need to install few django packages: 
- psycopg2 - to connect with PostgreSQL database
- django-cors-headers
- djangorestframework 

To do this use command:
```
pip install -r requirements.txt
```

#### Database configuration
You should run PortgreSQL server and create database, you can use the commands below

```
sudo -u postgres psql
CREATE DATABASE ticket_booking;
```
You can change database configuration in settings.py file to match your database.

To create tables based on models you can use migrations files and command:
```
python3 manage.py migrate
```

To run backend application type:
```
python3 manage.py runserver
```

### Running frontend project
```
cd /frontend/ticket_booking
```

You need to install Vue CLI package:
```
npm install -g @vue/cli
```
To run frontend application use command:
```
npm run serve
```
