# import pandas as pd
# print(pd.DataFrame(data = json_object))

import json, pandas

class Database:

    def read():
        # Opening JSON file
        with open('./Database/' + input('\n Type name.json. \n'), 'r') as json_file:
 
            # Reading from json file
            database = json.load(json_file)
    
        return database

    def write(database):
 
        # Serializing json
        json_file = json.dumps(database, indent=4)
 
        # Writing to .json
        with open('./Database/' + input('\n Type name.json. \n'), 'w') as outfile:
    
            outfile.write(json_file)

    def print(database):

        print(pandas.DataFrame(database))

class Operation:

    data = []

    def store(database):
        
        Operation.data.append(database)

    def clear():

        Operation.data.clear()

    def paycheck_sum():

        pass