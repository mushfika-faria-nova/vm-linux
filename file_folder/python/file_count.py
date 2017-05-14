fileread=input('filename: ')
try:

    file1=open(fileread)
except:
    print('file not found')
    exit()

count=0
for f in file1:
    count=count+1
    if f.startswith('From:'):
        print(f)
print('output' ,count)
