def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                return func().lower()
            else:
                return func().upper()
        return myinner
    return changecase
    
@changecase(1)
def myfunction():
    return "hello satish"
print(myfunction())
            