import urllib.request as ur
from bs4 import BeautifulSoup

url = 'http://www.jamnagar.org'
count = int(input('Enter count - '))
pos = int(input('Enter position - '))

for x in range(0,count):
	all_tags = []
	
	html = ur.urlopen(url).read()
	print(url)
	print('\n')
	
	soup = BeautifulSoup(html,"html.parser")
	tags = soup('a')
	
	for tag in tags:
		print(tag.get('href',None))
		all_tags.append(tag.get('href',None))
	
	print('\n')
	url = all_tags[pos - 1]
