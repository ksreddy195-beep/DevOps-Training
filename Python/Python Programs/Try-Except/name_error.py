try:
  print(x)
except NameError:
  print("varibale x is not defined")
except:
  print("something else went wrong")