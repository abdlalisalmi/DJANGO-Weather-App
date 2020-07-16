from django.shortcuts import render
from django.http import JsonResponse
import datetime

from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from django.views.decorators.csrf import csrf_exempt

from .API_keys import app_ID, consumer_key, consumer_secret


def get_city_weather(city=None, lat=None, lon=None):

    data = YahooWeather(APP_ID=app_ID,
                        api_key=consumer_key,
                        api_secret=consumer_secret)
    if city:
        weather = data.get_yahoo_weather_by_city(city, Unit.celsius)
    else:
        weather = data.get_yahoo_weather_by_location(lat, lon, Unit.celsius)

    if weather:
        sunny = [32, 36]
        cloudy = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        snowy = [5, 6, 7, 8, 9, 10, 14, 15, 16, 41, 42, 43, 46]
        stormy = [0, 1, 2, 3, 4, 11, 12, 13,
                  17, 18, 35, 37, 38, 39, 40, 45, 47]
        supermoon = [31, 33, 34, 44]

        # Get the location
        location = data.get_location().__dict__
        # print(condition)

        # Get the condition
        condition = data.get_condition().__dict__
        # print(condition)

        # Get the forecasts
        forecasts = []
        for day in data.get_forecasts():
            forecasts.append(day.__dict__)
        # print(forecasts)

        wind = data.get_wind()
        # print(wind.__dict__)

        humidity = data.get_atmosphere().__dict__['humidity']

        astronomy = data.get_astronomy().__dict__

        return {
            'location': location,
            'condition': condition,
            'forecasts': forecasts,
            'wind': wind,
            'humidity': humidity,
            'astronomy': astronomy,
            # icones
            'sunny': sunny,
            'cloudy': cloudy,
            'snowy': snowy,
            'stormy': stormy,
            'supermoon': supermoon,
            'today': datetime.datetime.now().strftime("%A"),
        }

    else:
        return {'error': True, 'city': city}


def home(request):
    template_name = 'home.html'
    context = {'search': False}
    if request.method == 'POST':
        city = request.POST['city']
        lat = request.POST['lat']
        lon = request.POST['long']
        if (city):
            context = get_city_weather(city=city)
        elif lat and lon:
            context = get_city_weather(lat=lat, lon=lon)
        context.update({'search': True})
    return render(request, template_name, context)


def API_used(request):
    template_name = 'pages/API_used.html'
    return render(request, template_name)


def contact(request):
    template_name = 'pages/contact.html'
    return render(request, template_name)
