# class Shark:
#     def swim(self):
#         print("The shark is swimming.")

#     def be_awesome(self):
#         print("The shark is being awesome.")

# sammy = Shark()
# #sammy.swim()
# #sammy.be_awesome()

# class Python_Switch():
    
#     def switch(self):

#         while True:
#             try:
#                 _switch = int(input('\n Type a number.' + '\n'))
#                 break
#             except ValueError:
#                 print("\n Invalid. Use valid number.")

#         return _switch
    
#     def day(self, month):

#         default = Python_Switch.default_error() #"Incorrect day"

#         return getattr(self, 'case_' + str(month), lambda: default)()
 
#     def default_error():

#         exit()

#     def case_1(self):
#         return "Jan"
 
#     def case_2(self):
#         return "Feb"
 
#     def case_3(self):
#         return "Mar"



# #print(Python_Switch.day(self, 1))
 
# #print(Python_Switch.day(3))

# #my_switch.switch()

# print(Python_Switch.day(Python_Switch.switch(self)))


# class Expando(object):
#     pass

# ex = Expando()
# ex.foo = 17
# ex.bar = "Hello"

# #Expando.fsa =

# Expando.fsx = [1, 2, Expando.fsa]

# print(ex.fsx[2].get('02').get('Salary per Month'))

import json

class O:

    data = []

    with open('./Database/' + input('\n Type database name. \n') + '.json', 'r') as json_file:
    
        database = json.load(json_file)

    def store(database):

        


print(type(data[0]))

print(data[0])