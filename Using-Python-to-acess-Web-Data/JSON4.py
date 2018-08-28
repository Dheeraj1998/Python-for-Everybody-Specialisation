import urllib.request as ur
import urllib.parse as up
import json

url = 'http://python-data.dr-chuck.net/geojson?'
address = input('Enter - ')

url = url + up.urlencode({'sensor':'false','address':address})
print(url)

jdata = json.loads(ur.urlopen(url).read())
print(jdata["place_id"])
