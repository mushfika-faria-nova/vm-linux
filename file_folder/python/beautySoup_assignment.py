from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
tags = soup('span')
#print (tags)
sum=0
for tag in tags:
    res= tag.contents[0]
    rr=int(res)
    sum=sum+rr
print (sum)
