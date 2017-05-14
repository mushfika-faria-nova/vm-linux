from functools import wraps

def decorator(function_to_use):
    @wraps(function_to_use)
    def wrapper(value):
        print ("you are calling {} with '{}' parameteres".format(function_to_use.__name__,value))
        return function_to_use(value)
    return wrapper

@decorator
def replace_comma_with_space(value):
    return value.replace(',', ' ')

print(replace_comma_with_space.__name__)
print(replace_comma_with_space.__module__)
print(replace_comma_with_space.__doc__)
print(replace_comma_with_space("my,commas,will,be,replaces,with,spaces"))
    
