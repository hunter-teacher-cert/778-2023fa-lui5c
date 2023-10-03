import json
import urllib.request

print("This program will tell you the phone number and Google Maps URL for the fire department in any city.")

url = "https://data.ny.gov/resource/qfsu-zcpv.json"
response = urllib.request.urlopen(url)
data_json = json.loads(response.read())

cities = []

# data_json is a list of json objects of each city
for result in data_json:
  cities.append(result['city'].lower())

# print(data_json)

city = input('Enter a city: > ')

if city.lower() in cities:
  result = data_json[cities.index(city.lower())]
  print(result['city'])
  print(result['phone_number'])
  print(result['address'])
  print(result['city'], result['st'], result['zip_code'])
  print(result['location_1'])
else:
  print("I don't have info on that city.")