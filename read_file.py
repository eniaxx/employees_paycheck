# import pandas as pd
# print(pd.DataFrame(data = json_object))

import json

def json_read():
    # Opening JSON file
    with open('./Database/' + input('\n Type name.json. \n'), 'r') as openfile:
 
        # Reading from json file
        json_object = json.load(openfile)
    
    return json_object