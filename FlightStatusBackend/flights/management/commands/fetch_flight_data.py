import requests
from django.core.management.base import BaseCommand
from flights.models import Flight
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch flight data from AviationStack API and store in the database'

    def handle(self, *args, **kwargs):
        url = 'http://api.aviationstack.com/v1/flights'
        params = {
            'access_key': 'd8350b842e7d843c5abc4d51fcfcea60',  # Replace with your actual API key
        }
        response = requests.get(url, params=params)
        data = response.json()

        for flight in data['data']:
            # Extract and transform data
            codeshare_info = flight['flight']['codeshared'] if flight['flight'].get('codeshared') else {}
            Flight.objects.create(
                flight_date=datetime.strptime(flight['flight_date'], '%Y-%m-%d'),
                number=flight['flight']['number'],
                iata=flight['flight']['iata'],
                icao=flight['flight']['icao'],
                status=flight['flight_status'],
                airline=flight['airline']['name'],
                departure_airport=flight['departure']['airport'],
                departure_city=flight['departure'].get('timezone', ''),
                departure_iata=flight['departure']['iata'],
                departure_icao=flight['departure']['icao'],
                departure_terminal=flight['departure'].get('terminal', ''),
                departure_gate=flight['departure'].get('gate', ''),
                departure_scheduled=datetime.strptime(flight['departure']['scheduled'], '%Y-%m-%dT%H:%M:%S%z'),
                departure_estimated=datetime.strptime(flight['departure']['estimated'], '%Y-%m-%dT%H:%M:%S%z') if flight['departure']['estimated'] else None,
                departure_actual=datetime.strptime(flight['departure'].get('actual', ''), '%Y-%m-%dT%H:%M:%S%z') if flight['departure'].get('actual') else None,
                departure_runway=datetime.strptime(flight['departure'].get('estimated_runway', ''), '%Y-%m-%dT%H:%M:%S%z') if flight['departure'].get('estimated_runway') else None,
                arrival_airport=flight['arrival']['airport'],
                arrival_city=flight['arrival'].get('timezone', ''),
                arrival_iata=flight['arrival']['iata'],
                arrival_icao=flight['arrival']['icao'],
                arrival_terminal=flight['arrival'].get('terminal', ''),
                arrival_gate=flight['arrival'].get('gate', ''),
                arrival_baggage=flight['arrival'].get('baggage', ''),
                arrival_scheduled=datetime.strptime(flight['arrival']['scheduled'], '%Y-%m-%dT%H:%M:%S%z'),
                arrival_estimated=datetime.strptime(flight['arrival']['estimated'], '%Y-%m-%dT%H:%M:%S%z') if flight['arrival']['estimated'] else None,
                arrival_actual=datetime.strptime(flight['arrival'].get('actual', ''), '%Y-%m-%dT%H:%M:%S%z') if flight['arrival'].get('actual') else None,
                arrival_runway=datetime.strptime(flight['arrival'].get('estimated_runway', ''), '%Y-%m-%dT%H:%M:%S%z') if flight['arrival'].get('estimated_runway') else None,
                delay=flight.get('delay'),
                codeshare_airline_name=codeshare_info.get('airline_name', ''),
                codeshare_airline_iata=codeshare_info.get('airline_iata', ''),
                codeshare_airline_icao=codeshare_info.get('airline_icao', ''),
                codeshare_flight_number=codeshare_info.get('flight_number', ''),
                codeshare_flight_iata=codeshare_info.get('flight_iata', ''),
                codeshare_flight_icao=codeshare_info.get('flight_icao', ''),
            )
