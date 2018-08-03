import json

f = open("allanswers.json","r")
data=json.load(f)
print(data)
f.close()
