def changecase(func):
    def myinner():
        return func().upper()
    return myinner
    
@changecase
def myfunction():
    return "Hello satish"
@changecase
def otherfunction():
    return "i am bad"
print(myfunction())
print(otherfunction())