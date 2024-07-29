# Generated by Django 5.0.3 on 2024-07-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_time',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_number',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_actual',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_baggage',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_estimated',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_gate',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_iata',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_icao',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_runway',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_scheduled',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_terminal',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='codeshare_airline_iata',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='codeshare_airline_icao',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='codeshare_airline_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='codeshare_flight_iata',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='codeshare_flight_icao',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='codeshare_flight_number',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='delay',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_actual',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_estimated',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_gate',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_iata',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_icao',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_runway',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_scheduled',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_terminal',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='flight',
            name='iata',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='icao',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_airport',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_airport',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=models.CharField(default='scheduled', max_length=20),
        ),
    ]
