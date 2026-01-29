def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner
@changecase
def myfunction(name):
    return "hello " + name
print(myfunction("john"))
