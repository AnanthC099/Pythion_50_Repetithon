# Code Fragment 1 - Nested function accessing enclosing scope variable

def outer():
    num = 500
    def inner():
        print(num)
    inner()

outer()

# Code Fragment 2 - Nested function with locals() inspection

def outer():
    num = 500
    def inner():
        print('inner():Entered')
        print('inner():locals():', locals())
        print(num)
    inner()

outer()
