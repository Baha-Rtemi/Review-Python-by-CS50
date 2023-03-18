# announce a function hello() (( which mean make something before & after the function work ))
def announce(f):
    # define wrapper function
    def wrapper():
        print("before the function is running ...  ...  ... ".title())
        f()
        print(" ...  ...  ... after the function is running.".title())
    # return wrapper function
    return wrapper
# announce a function before it's start
# function hello()
@announce # to announce the function hello()
def hello():
    print(">>>   the function is running.   <<<".upper())

# but there is something will happpen before it.
# call the function hello()
hello()
# also there is something will happpen afetr it.