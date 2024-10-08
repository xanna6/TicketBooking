# Generated by Django 5.0.3 on 2024-07-31 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('rows', models.IntegerField(blank=True, null=True)),
                ('seats_in_row', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HallScreeningTime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hall_screening_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.hallscreeningtime')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tickets.movie')),
            ],
        ),
    ]
