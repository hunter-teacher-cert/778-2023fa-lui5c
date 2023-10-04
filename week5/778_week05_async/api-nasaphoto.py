import json
import urllib
import imutils
import cv2
import pandas

# use the NASA API database
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = urllib.request.urlopen(url)
data_json = json.loads(response.read())

# I used: https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi
# have pandas read the dictionary in data_json
df = pandas.DataFrame.from_records([data_json])

# print the raw JSON data just for display purposes
print("Raw JSON data from NASA:")
print(data_json)
print("")

# the NASA photo of the day URL
print("Address of the NASA Photo of the day:")
print(data_json['url'])

# download an image from the NASA website URL
img = imutils.url_to_image(data_json['url'])


# for resize i benefited from this discussion:
# https://stackoverflow.com/questions/35180764/opencv-python-image-too-big-to-display
photo_scale = 0.5

# Display the image and pause for ESC
cv2.imshow(data_json['title'] + ' ' + data_json['date'], 
           cv2.resize(img, 
                      (int(img.shape[:2][0]*photo_scale), 
                       int(img.shape[:2][1]*photo_scale)
                      )))
cv2.waitKey(0)