# Generated by Django 5.0.3 on 2024-08-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0005_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
