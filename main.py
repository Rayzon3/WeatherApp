import requests
from pprint import pprint



def find_city_weather():
    city = input('Enter your city : ')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid= [SORRY CANT SHOW MY KEY] &units=metric'.format(city)

    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))

find_city_weather()
