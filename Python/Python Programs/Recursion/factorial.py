def factorial(n):
    #base case
    if n == 0 or n == 1:
        return 1
    #recursive case
    else:
        return n * factorial(n-1)
print(factorial(5))