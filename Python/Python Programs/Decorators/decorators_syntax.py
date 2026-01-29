def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "hello satish"
print(myfunction())