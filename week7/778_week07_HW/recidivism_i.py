import json
import urllib.request
import urllib.parse

import espeak

espeak.init()
speaker = espeak.Espeak()
speaker.rate = 100

print("This program will prompt you for a county, and then show you recidivism statistics for that county.")
speaker.say("This program will prompt you for a county, and then tell you recidivism statistics for that county. PRess enter to continue. ")
input()

speaker.say("Enter a county. For example, nassau.")
county = input('Enter a county: (eg. \'nassau\')> ')

safeletters = "?&=$><"

url = "https://data.ny.gov/resource/y7pw-wrny.json" + urllib.parse.quote(f"?county_of_indictment={county.upper()}&$order=release_year", safe=safeletters)
#print(url)
#input()
response = urllib.request.urlopen(url)
temp_data_json = json.loads(response.read())

data_json = [] + temp_data_json

offset = 1000

while len(temp_data_json) == 1000 and temp_data_json != []:
  add_url= "https://data.ny.gov/resource/y7pw-wrny.json" + urllib.parse.quote(f"?county_of_indictment={county.upper()}&$order=release_year&$offset={offset}", safe=safeletters)
  add_response = urllib.request.urlopen(add_url)
  temp_data_json = json.loads(add_response.read())
  data_json = data_json + temp_data_json
  offset += 1000
  
to_say = []

if data_json == []:
  print("I couldn't find any data for that county.")
  to_say.append("I couldn't find any data for that county.")
else:
  statuses = {}
  for p in data_json:
    if p['return_status'] in statuses:
      statuses[p['return_status']] += 1
    else:
      statuses[p['return_status']] = 1
  print(f"The recidivism breakdown for {county.title()} is as follows:")
  to_say.append(f"The recidivism breakdown for {county.title()} is as follows. ")  
  for key in statuses:
    print(key, f'({int(100*statuses[key]/sum(statuses.values()))}%)')
    to_say.append(f'{key} ({int(100*statuses[key]/sum(statuses.values()))}%). ')
    
    
          
amt = min(6, len(to_say))
speaker.say(f"Press enter to hear the first {amt-1} results. ")
input()
speaker.say("".join(to_say[:amt+1] + ["Press enter to exit."]))
input()
  