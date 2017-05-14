def my_function(constant):
    def inner(foo):
        print (constant ,foo)
        return foo + constant
    return inner
    
plus_one = my_function(1)
print(str(plus_one(2)))
