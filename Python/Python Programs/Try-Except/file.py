try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("something went wring when opening the file")