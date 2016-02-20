import urllib.request
from bs4 import BeautifulSoup


#url = 'http://python-data.dr-chuck.net/comments_42.html' #input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_245630.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
total = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:',tag)
    #print('URL:',tag.get('href', None))
    print('Contents:',int(tag.contents[0]))
    #print('Attrs:',tag.attrs)
    total = total + int(tag.contents[0])
    print('Total is ',total)

