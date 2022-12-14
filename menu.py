import data_operations as do

class Print_Menu():

	def menu(choice):

		match choice:
			
			case 'Start':
				
				print(open('./Menu/start_menu.txt').read())
			
			case 'Employee':

				print(open('./Menu/employee_menu.txt').read())

#Start Menu Class with __init__, __err__, which_case, case_0 to case_6
class Start_Menu:
	
	#Initialazing the Start Menu class
	def __init__():
	
		Print_Menu.menu('Start')

		Start_Menu.which_case(Case.choice())
	
	#Function for handling int input error (no case available), default action
	def __error__():

		print('\n Incorrect choice.')

		return Start_Menu.which_case(Case.choice())
	
	#This function switch between cases
	def which_case(argument):

		case = 'case_' + str(argument)

		print('\n' + case)
		
		default = Start_Menu.__error__

		return getattr(Start_Menu, case, default)()

	#Defined case functions and their behavior
	def case_0():

		print('\n See you soon.')

		exit()

	def case_1():
		
		file_name = do.Database.database_name()

		file_data = do.Database.read(file_name)

		do.Operation.store(file_name, file_data)

	def case_2():
		
		Employee_Menu.__init__()

	def case_3():
		
		exit()

	def case_4():
		
		exit()
	
	def case_5():
		
		exit()
	
	def case_6():
		
		exit()

#Employee Menu Class with __init__, __err__, which_case, case_0 to case_6
class Employee_Menu:

	#Initialazing the Employee Menu class
	def __init__():
	
		Print_Menu.menu('Employee')

		Employee_Menu.which_case(Case.choice())

	#Function for handling int input error (no case available), default action
	def __error__():

		print('\n Incorrect choice.')

		return Employee_Menu.which_case(Case.choice())

	#This function switch between cases
	def which_case(argument):

		case = 'case_' + str(argument)

		print('\n' + case)
		
		default = Employee_Menu.__error__

		return getattr(Employee_Menu, case, default)()

	#Defined case functions and their behavior
	def case_0():

		Start_Menu.__init__()

	def case_1():
		
		exit()

	def case_2():
		
		exit()

	def case_3():
		
		exit()

	def case_4():
		
		exit()
	
	def case_5():
		
		exit()
	
	def case_6():
		
		exit()

#Class for taking valid int input
class Case:

	def choice():
		#infinite loop with exception for anything else than int and break
		while True:
			try:
				argument = int(input('\n Type a number' + '\n'))
				break
			except ValueError:
				print('\n Invalid. Use valid number.')
		return argument