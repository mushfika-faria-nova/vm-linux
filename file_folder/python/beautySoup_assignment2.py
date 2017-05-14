from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter - ')
count = input('Enter count - ')
#position = input('Enter position - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for tag in tags:
    print('URL:', tag.get('href',None))
    count=count-1
