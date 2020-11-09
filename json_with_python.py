# use json module to do json encoding and decoding

import json

car_data = {"name": "tesla", "engine": "electric"}
#creating a dictionary and storing it into a variable
# print(type(car_data))

# json.dumps - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))
print(car_data_json_string)

# This is how we can encode from a dictionary and write to a file
with open("new_json_file.json", "w+") as jsonfile:
    json.dump(car_data, jsonfile, sort_keys=True)  # json.dump() - creates a stream object and except a file object to write to

with open("new_json_file.json", "r") as jsonfile:
    car = json.load(jsonfile) # load() copies the data and stores into a variable
    print(type(car))
    print(car["name"])
    print(car["engine"])
# getting the value by key

# Json is used heavily in the industry, so reading, writing, parsing and converting data are the most commonly utilised options
