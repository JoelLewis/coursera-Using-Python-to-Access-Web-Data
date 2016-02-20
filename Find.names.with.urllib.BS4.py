# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib.request
from bs4 import BeautifulSoup

#url = input('Enter - ')
#pos = input('Enter position - ') - 1
#reps = [range(input('Enter repetitions - '))

#intialize 
pos = 17 #for test 2
reps = range(7) #for test .... range(4)
output = []
#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html' #for test
url = 'http://python-data.dr-chuck.net/known_by_Caidyn.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')



# Retrieve each name in chain 
for _ in reps:
	#Print Name in position
	print(tags[pos].contents)
	#reload soup for next rep
	print('Retrieving: ',tags[pos].get('href'))
	url = tags[pos].get('href')
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')
	

