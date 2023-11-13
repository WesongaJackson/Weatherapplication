from django.shortcuts import render
import json
import requests
from datetime import datetime
from Weather import settings


# Create your views here.
def home(request):
    try:
        if request.method=="POST":
            API_KEY= settings.API_KEY
            city_name =request.POST.get('city')
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            response=requests.get(url).json()
            current_time=datetime.now()
            formatted_time=current_time.strftime("%a, %b %d %Y, %I:%M:%S %p")
            city_weather={
               'city':city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
                }
            
        else:
            city_weather={}
            
        return render(request,'Main/home.html',{'city_weather':city_weather})
    except:
        return render(request, 'Main/404.html')
     
    
