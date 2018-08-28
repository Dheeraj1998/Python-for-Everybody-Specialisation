import urllib.request as ur
from bs4 import BeautifulSoup

url = 'http://www.google.com'

html = ur.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

tags = soup('a')

for tag in tags:
	print(tag.get('href',None))
