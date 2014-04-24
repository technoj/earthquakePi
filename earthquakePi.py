#!/usr/local/bin/python2.7
    
import urllib, json
url = "http://earthquake.usgs.gov/earthquakes/feed/v1
.0/summary/all_hour.geojson"
responce = urllib.urlopen(url);
data = json.loads(responce.read())
for i, object in enumerate(data['features']):
  newValue = i, object['properties']['mag'];
  if (newValue > 4):
   print("it works!")
  else:
   print("maybe not")
