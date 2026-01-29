def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function("Hello", "emil", "tobias", "finn")
