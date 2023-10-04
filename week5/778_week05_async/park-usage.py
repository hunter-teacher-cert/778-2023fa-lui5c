import json
import urllib.request

print("This program will prompt you for a county, and then help you explore the attendance of the NY State parks in that county.")

county = input('Enter a county: (eg\'kings\')> ')

url_county = county.title().replace(" ", "%20")

url = f"https://data.ny.gov/resource/8f3n-xj78.json?county={url_county}&year=2022"
response = urllib.request.urlopen(url)
data_json = json.loads(response.read())

if data_json == []:
  print("I couldn't find any data for that county.")
else:
  print(f"I found the following parks in {county.title()} county:")
  count = 1
  for p in data_json:
    print(f"{count}\t{p['facility']}")
    count += 1
  which = int(input("type the number of the facility that you would like to find the attendance of."))
  if which-1 < len(data_json) and which > 0:
    print("The attendance of", data_json[which-1]['facility'], "was", data_json[which-1]['attendance'], "in 2022.")