#First attempt - CLI program: employees & salary
	
def write():	
	
	_input = input("Type the input: \n")
	print(_input + '\n') 
	print(type(_input))
	
	switch()
	
def switch():
	
	_switch = input('\n Again, y or n ? \n')
		
	if _switch == "y":	
		
		write()

	elif _switch != "y" and _switch != "n":
		
		print('\n Use y or n')
		
		switch()
			
	else:
		
		print('\n' + 'Goodbye.')
		
		exit()