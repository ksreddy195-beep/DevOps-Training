def changecase(fun):
    def myinner():
        return fun().upper()
    return myinner
@changecase
def myfunction():
    return "what a life"
print(myfunction.__name__)