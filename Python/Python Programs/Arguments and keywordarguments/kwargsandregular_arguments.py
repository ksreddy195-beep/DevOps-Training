def my_function(username, **details):
  print("username:", username)
  print("additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function("emil123", age = 25, city = "oslo", hobby = "coding")    