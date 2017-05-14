import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 
#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
 
url=input('Enter url: ')

print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
#print ('Retrieved',len(data),'characters')
#    print (data)
tree = ET.fromstring(data)


results = tree.findall('comments/comment')
counts = tree.findall('.//count')
print (counts)
#print (results)
sum=0
for item in results:
    sum=sum+int( item.find('count').text)
print (sum)
sum=0
for item in counts:
   sum = sum + int(item.text)

# sum=sum+int( item.find('count').text)
print ("Again sum : ",sum)

