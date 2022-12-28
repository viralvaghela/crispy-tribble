import requests
city = input("Enter the city name: ")
KEY = 'YOUR_API_KEY'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
    city, KEY)
print(url)
response = requests.get(url)
data = response.json()
temp = data['main']['temp']
weather = data['weather'][0]['main']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']

print("Temperature: {} degree celcius".format(temp))
print("Weather: {}".format(weather))
print("Humidity: {}".format(humidity))
print("Wind Speed: {}".format(wind_speed))
print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))
