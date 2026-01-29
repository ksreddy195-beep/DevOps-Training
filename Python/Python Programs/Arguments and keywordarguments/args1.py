def my_function(*args):
    print("type:", type(args))
    print("first argument:", args[0])
    print("second argument:", args[1])
    print("all arguments:", args)
my_function("emil", "tobia", "finn")