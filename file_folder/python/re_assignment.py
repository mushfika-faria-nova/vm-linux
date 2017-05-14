import re

fname=input('enter filename:\n')
if len(fname)<1 : fname='regex_sum_364264.txt'
fhandle=open(fname)
sum=0
for line in fhandle:
    data=re.findall('[0-9]+',line)
    if len(data)>0:
      #print (data)
       for w in data:
           red=int(w)
           sum=sum+red
print (sum)        
