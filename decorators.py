#decorators

def  announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("Done with the function")
        
    return wrapper


@announce
def hello():
    print("this is the hello function")

hello()