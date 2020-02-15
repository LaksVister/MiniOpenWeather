"""Current temperature in city"""
import requests

city = input("City? ")
if not city:
    city = 'Kiev'  # default city, just press enter

api_key = '00d8cfc15e00563c54b8f53919c25083'
api_url = 'http://api.openweathermap.org/data/2.5/weather'
units = 'metric'
lang = 'ua'

params = {
    'q': city,
    'appid': api_key,
    'units': units,
    'lang': lang,
}

res = requests.get(api_url, params=params)
print(res)
# breakpoint()
data = res.json()
print(data)
try:
    print(f"Current temperature in {city} is {data['main']['temp']} °C")
except KeyError:
    print("City not found")

for weather in data['weather']:
    print(weather['description'])
