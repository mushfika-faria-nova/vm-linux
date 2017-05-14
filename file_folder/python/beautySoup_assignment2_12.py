
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter - ')
count = input('Enter count - ')
pos=input('enter pos:')
      
html=urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')



