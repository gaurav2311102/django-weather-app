import requests
from django.shortcuts import render
from .forms import Cityform
from django.conf import settings

def weather_view(request):
    weather_data = {}
    form = Cityform(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = settings.WEATHER_API_KEY
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            else:
                weather_data['error'] = 'City not found.'


    return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})
