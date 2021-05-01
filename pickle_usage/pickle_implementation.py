import pickle
import json
from bs4 import BeautifulSoup

# Data to be written
dictionary ={
"id": "04",
"name": "sunil",
"depatment": "HR"
}

'''
dumps() method can convert a python object into a JSON/Pickle string
dump() method can be used for writing to JSON/Pickle file 
'''

# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)

# Serializing pickle
pickle_object = pickle.dumps(dictionary)
print(pickle_object)


# Serializing json and writing to a file
with open("pickle_usage/sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

# Serializing pickle and writing to a file
with open("pickle_usage/pickledata", "wb") as outfile:
    pickle.dump(dictionary,outfile)

# De-Serializing json
# Output of Json
print(json.loads(json_object))

# De-Serializing pickle
# Output of pickle
print(pickle.loads(pickle_object))

# De-Serializing json from a file
# Output of Json file
with open("pickle_usage/sample.json", "r") as outfile:
    print(json.load(outfile))

# De-Serializing pickle from a file
# Output of pickle file
with open("pickle_usage/pickledata", "rb") as outfile:
    print(pickle.load(outfile))