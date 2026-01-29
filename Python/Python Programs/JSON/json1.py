import json

x = '{"name":"john", "age":30, "city":"new york"}'
y = json.loads(x)

print(y["age"])