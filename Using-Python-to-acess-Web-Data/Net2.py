import urllib.request as ur

fhand = ur.urlopen('http://python-data.dr-chuck.net')

for line in fhand:
	print(line.strip())
