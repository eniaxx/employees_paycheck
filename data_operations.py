import os, json, pandas, menu

class Database:

    def list_Database():
    
        dir = './Database'

        print(pandas.DataFrame(data = os.listdir(dir)))

    def database_name():

        Database.list_Database()

        json_file = input('\n Type database name. \n')

        return json_file

    def read(name):
        
         # Opening JSON file
        with open('./Database/' + name + '.json', 'r') as _name:

        # Reading from json file
            database = json.load(_name)
    
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

    cached_data = {}

    def store(name, database):
        
        Operation.cached_data[name] = database

        print(pandas.DataFrame(data= Operation.cached_data[name]))

    def clear():

        Operation.cached_data.clear()

    def empty_database_check():

        while Operation.cached_data is True:
            
            try:
                return True
                
            except ValueError:

                print("\n Invalid. You didn't load a database.")

                menu.Start_Menu.__init__()
        
        #return something(data)