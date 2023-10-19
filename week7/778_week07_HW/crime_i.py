import json
import urllib.request
import espeak

espeak.init()
speaker = espeak.Espeak()
speaker.rate = 100

print("This program will prompt you for a county, and then give you inmate information about that county.")
speaker.say("This program will prompt you for a county, and then give you inmate information about that county. Press enter to continue.")
input()


speaker.say("Enter a county. For example, Albany. Then, press enter.")
county = input('Enter a county: (eg. \'albany\')> ')

url_county = county.upper().replace(" ", "%20")

url = f"https://data.ny.gov/resource/55zc-sp6m.json?county_of_indictment={url_county}&snapshot_year=2023&$order=current_age"
response = urllib.request.urlopen(url)
temp_data_json = json.loads(response.read())

data_json = [] + temp_data_json

offset = 1000

while len(temp_data_json) == 1000 and temp_data_json != []:
  add_url= f"https://data.ny.gov/resource/55zc-sp6m.json?county_of_indictment={url_county}&snapshot_year=2023&$order=current_age&$offset={offset}"
  add_response = urllib.request.urlopen(add_url)
  temp_data_json = json.loads(add_response.read())
  data_json = data_json + temp_data_json
  offset += 1000
  
to_say = []

if data_json == []:
  print("I couldn't find any data for that county.")
  to_say.append("I couldn't find any data for that county. ")
else:
  print(f"I found the following inmates in {county.title()} county:")
  to_say.append(f"I found the following inmates in {county.title()} county. Here are their ages and most serious crimes. ")
  count = 1
  print("\tage\tmost serious crime")
  for p in data_json:
    print(f"{count}\t{p['current_age']}\t{p['most_serious_crime']}")
    to_say.append(f"{count}\t{p['current_age']}\t{p['most_serious_crime']}. ")
    count += 1
          
          
amt = min(6, len(to_say))
speaker.say(f"Press enter to hear the first {amt-1} results. ")
input()
speaker.say("".join(to_say[:amt+1] + ["Press enter to exit."]))
input()