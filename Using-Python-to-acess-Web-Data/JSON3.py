import json
import urllib.request as ur

url = 'http://localhost/Sample_Files/comments_17041.json'
data = ur.urlopen(url).read()
jfile = json.loads(data)
total_sum = 0

for x in range(0,len(jfile["comments"])):
	total_sum = total_sum + int(jfile["comments"][x]["count"])

print(total_sum)
