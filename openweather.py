#!/usr/bin/env python3

import requests
import json

api = input('Enter your api key from openweather: ')

city = input('Enter name of city: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}'

r = requests.get(url)
resp = json.loads(r.text)

if r.status_code == 200:
    print(f"\nIt is {resp['main']['temp']}°C but it feels like {resp['main']['feels_like']}°C")
elif r.status_code == 401:
    print('Get a valid Api key!')
else:
    print(f'Error {r.status_code}')
