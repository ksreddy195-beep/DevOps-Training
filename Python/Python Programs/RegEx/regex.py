import re

txt = "The rain in spain"
x = re.search("^The.*Spain$", txt)
print(x)