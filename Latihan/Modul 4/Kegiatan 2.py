def uppercase_decorator(function):
    def wrapper():
        func_result = function()
        make_uppercase = func_result.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)
