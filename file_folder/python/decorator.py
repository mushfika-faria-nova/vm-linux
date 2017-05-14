def decorator(function_to_use):
    def wrapper(value):
        print("you are calling {} with ' {} ' as parameter" .format(function_to_use.__name__,value))
        return function_to_use(value)
    return wrapper

def replace_function(value):
     return value.replace(',', ' ' )

functionuse=decorator(replace_function)
print(functionuse("my,commas,will,be,replaces,with,spaces"))
 
