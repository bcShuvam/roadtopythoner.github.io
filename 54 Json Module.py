import json
#json = JAvaScript Object Notation
data = '{"var1":"Harry","var2":56}'
print(data)

parsed = json.loads(data)
print(parsed)

######################################

# Python program to read
# json file

# Opening JSON file
f = open('data.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()


######################################

data2 = {
    "channel_name":"Clash of Lunatics",
    "cars":['bmw','audi a8','ferrari'],
    "bikes":('Kawasaki','Suzuki','Honda'),
    "is_bad":False
}

py_to_js = json.dumps(data2) # It converts Python code into Javascript code
print(py_to_js)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))