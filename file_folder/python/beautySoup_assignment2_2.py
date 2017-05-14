from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter - ')
count = input('Enter count - ')
pos=input('enter pos:')
while count >= 0:
 
    html=urlopen(url).read() 
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print (tags)
    print('URL:', tags[pos].get('href',None))
    count=count-1

