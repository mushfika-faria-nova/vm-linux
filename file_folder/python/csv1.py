import csv
with open('my.csv', 'r+', newline='') as csv_file:
    reader=csv.reader(csv_file)
    for r in reader:
       print (str(r))

    
