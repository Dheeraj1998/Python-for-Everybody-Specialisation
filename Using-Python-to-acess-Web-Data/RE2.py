import re

entire_text = open('regex-sum.txt')
total_sum = 0

for line in entire_text:
	match_text = re.findall('[0-9]+',line)
	
	for num in match_text:	
		total_sum = total_sum + int(num)

print(total_sum)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)

print(y)

text_string = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
