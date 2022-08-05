#thislist = ["apple", "banana", "cherry"]
#tropical = ["mango", "pineapple", "kiwi", "papaya"]
#thislist.extend(tropical)
#print("\n", str(thislist), "\n")

#x = thislist.__len__()
    
#for i in range(0, thislist.__len__()):
#    print(thislist[i])

import json

my_details = {
    'name': 'John Doe',
    'age': 29
}

with open('personal.json', 'w') as json_file:
    json.dump(my_details, json_file)

f = open('personal.json')

data = json.load(f)

for i in data['emp_details']:
    print(i)

f.close()