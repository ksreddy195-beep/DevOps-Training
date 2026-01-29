def my_function(**myvar):
  print("type:", type(myvar))
  print("name:", myvar["name"])
  print("age:", myvar["age"])
  print("all data:", myvar)

my_function(name = "tobias", age = 30, city = "belgium")