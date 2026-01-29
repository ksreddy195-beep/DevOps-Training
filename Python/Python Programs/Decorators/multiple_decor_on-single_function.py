def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "hello " + func() + "have a good day"
    return myinner
@changecase
@addgreeting
def myfunction():
    return "satish"
print(myfunction())