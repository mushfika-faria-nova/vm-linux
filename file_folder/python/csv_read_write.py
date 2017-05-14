import csv
def read_file(file_location):
    with open (file_location,'r+',newline='') as csv_file:
        reader=csv.reader(csv_file)
        return [row for row in reader]

def write_file(file_location,rows):
    with open(file_location,'w+',newline='') as csv_file:
        writer=csv.writer(csv_file)
        for row in rows:
            writer.writerow(row)

def test():
    col=int(input('number of columns:'))
    inp_row=[]
    keepgo=True
    while keepgo:
        inp_row.append([input('coloumn {}: '.format(i+1)) for i in range(0,col)])
        keepgo2=input('keep going? (y/n):')
        if keepgo2 !='y':
            keepgo=False

    print (str(inp_row))
    write_file('raw.csv',inp_row)
    written_value = read_file('raw.csv')
    print(str(written_value))

test()
    
