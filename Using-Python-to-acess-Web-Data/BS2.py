import urllib.request as ur
from bs4 import BeautifulSoup

url = 'http://localhost/HTML_Docs/comments_17040.html'

html = ur.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
total_sum = 0

for tag in tags:
	total_sum = total_sum + int(tag.contents[0])

print(total_sum)
