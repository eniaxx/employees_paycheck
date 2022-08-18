
from asyncio.windows_events import NULL
import json
 
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

employee = {'E01' : dictionary, 'E02' : dictionary, 'E03' : NULL}
 
# Serializing json
json_object = json.dumps(employee, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)