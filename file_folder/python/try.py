from urllib.request import urlopen
from bs4 import BeautifulSoup
url =None 
for i in range(7):
    if url is None:
        url = input('ENter Url : ')
    else:
        url = tag.get('href', None)
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    tag = soup('a')[17]
    name = tag.contents[0]
    print(name)
