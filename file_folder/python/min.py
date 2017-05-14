def mina():
    count=0
    string1=input('input string:\n')
    chars=input('character:\n')

    for i in string1:
        if i==chars:
            count=count+1
    print(count)
    
mina()
