
def announce(f):
    def wrapper():
        print("The funcation about to run")
        f()
        print("The funcation done running")
    return wrapper
@announce
def hello():
    print("Hello, World!")

hello()