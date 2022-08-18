from menu import *
from list_dir import *
from read_file import *
import pandas as pd

#def write():	
	
#	_input = input("\n Type the input: \n")
	#print(_input + '\n') 
	#print(type(_input))
	
#	switch()
	
def start_menu_switch():
	
	start_menu()

	while True:
		try:
			_switch = int(input('\n Type a number.' + '\n'))
			break
		except ValueError:
			print("\n Invalid. Use valid number.")
		
	if _switch == 0:	
		
		print('\n' + 'See you soon.')

		exit()

	elif _switch == 1:

		print("\n You've choosen 1. \n Choose json file.\n")

		list_Database()

		print(pd.DataFrame(json_read()))

		start_menu_switch()

	elif _switch == 2:
		
		#print("\n You've choosen 2")

		employee_menu_switch()

	elif _switch == 3:
		
		print("\n You've choosen 3")
		
		start_menu_switch()

	elif _switch == 4:
		
		print("\n You've choosen 4")
		
		start_menu_switch()

	elif _switch == 5:
		
		print("\n You've choosen 5")
		
		start_menu_switch()

	elif _switch == 6:
		
		print("\n You've choosen 6")
		
		start_menu_switch()

	else:
		
		print('\n' + 'Invalid.')
		
		start_menu_switch()


def employee_menu_switch():
	
	employee_menu()

	while True:
		try:
			_switch = int(input('\n Type a number' + '\n'))
			break
		except ValueError:
			print("\n Invalid. Use valid number.")
		
	if _switch == 0:	
		
		#print('\n' + 'See you soon.')
		#exit()

		start_menu_switch()

	elif _switch == 1:
		
		print("\n You've choosen 1")

		employee_menu_switch()

	elif _switch == 2:
		
		print("\n You've choosen 2")

		employee_menu_switch()

	elif _switch == 3:
		
		print("\n You've choosen 3")
		
		employee_menu_switch()

	elif _switch == 4:
		
		print("\n You've choosen 4")
		
		employee_menu_switch()

	elif _switch == 5:
		
		print("\n You've choosen 5")
		
		employee_menu_switch()

	elif _switch == 6:
		
		print("\n You've choosen 6")
		
		employee_menu_switch()

	else:
		
		print('\n' + 'Invalid.')
		
		employee_menu_switch()