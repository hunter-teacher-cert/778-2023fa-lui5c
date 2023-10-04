import json
import urllib.request
import urllib.parse

print("This program will prompt you for an age, and then give you inmate security information about all of the inmates at or older than that age.")

age = int(input('Enter an age: (eg. \'67\')> '))

safeletters = "?&=$><"

url = "https://data.ny.gov/resource/55zc-sp6m.json" + urllib.parse.quote(f"?$where=current_age > {age}&snapshot_year=2023&$order=current_age", safe=safeletters)
#print(url)
#input()
response = urllib.request.urlopen(url)
temp_data_json = json.loads(response.read())

data_json = [] + temp_data_json

offset = 1000

# for when the payload with the free api key isn't enough
# and we need to get more data to get the full query
while len(temp_data_json) == 1000 and temp_data_json != []:
  add_url= "https://data.ny.gov/resource/55zc-sp6m.json" + urllib.parse.quote(f"?$where=current_age > {age}&snapshot_year=2023&$order=current_age&$offset={offset}", safe=safeletters)
  add_response = urllib.request.urlopen(add_url)
  temp_data_json = json.loads(add_response.read())
  data_json = data_json + temp_data_json
  offset += 1000

if data_json == []:
  print("I couldn't find any data for that age.")
else:
  lvl_amt = {}
  for p in data_json:
    if p['facility_security_level'] in lvl_amt:
      lvl_amt[p['facility_security_level']] += 1
    else:
      lvl_amt[p['facility_security_level']] = 1
  print("The facility security breakdown for inmates aged",age,"and older is as follows:")
  for key in lvl_amt:
    print(key, f'({int(100*lvl_amt[key]/sum(lvl_amt.values()))}%)')
  