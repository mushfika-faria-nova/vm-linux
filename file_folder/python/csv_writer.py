import csv
rows=[['1', '2', '3'], ['4', '5', '6']]
with open('my1.csv', 'w+', newline='') as csv_file:
    writer=csv.writer(csv_file)
#    for r in rows:
    writer.writerows(rows)

with open('my1.csv','r+',newline='') as csv_file:
    reader=csv.reader(csv_file)
    for r in reader:
       print (str(r))
