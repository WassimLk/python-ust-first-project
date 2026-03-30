_time=[]
_tasks=[]
_my_dictionary = {}
_choice = ''


def line():
	print('---------------------------')

def show_menu():
	line()
	print('          MENU        ')
	line()
	print('1. Add item')
	print('2. Mark as done')
	print('3. View list')
	print('4. Exit')
	line()
	local_choice = input('Enter your choice: ')
	return local_choice

#Warning : time should 0 and 23 for the hours, and between 0 and 59 for minutes
def time_setting():
	while True:  #Infinite loop until the user give a valid input. The 'return' stops the loop.
		time = int(input("Enter your time in HHMM format"))
		if not time:
			print("You did not type anything. Please try again.")
			continue
		if not isinstance(time, int):
			print("Time must be an integer!")
			continue
		if len(str(time)) != 4:
			print("You did not type a valid time. Please try again.")
			continue
		if time //100 < 0 or time //100 > 23 or time %100 < 0 or time %100 > 59:
			print("Time must be between 0 and 23 for the hours, and between 0 and 59 for the minutes.")
			continue
		return time

def task_setting():
	while True:
		item = input('What is to be done? ')
		if not item:
			print("You did not type anyhting. Please try again")
			continue
		return item
	
def del_task(): #deleting an item from my to-do-list
	item = input('What is to be marked as done? ')
	if item in _my_dictionary:
		_my_dictionary.pop(item)
		print(item,"done!")
	else:
		print('Could not find item', item)
		

while _choice != '4':
	choice = show_menu()
	if choice == '1':
		key = time_setting()
		value = task_setting()
		_time.append(key)
		_tasks.append(value)
		_my_dictionary = dict(zip(_time, _tasks))
		print("The task", value, " is scheduled for", key)
		
	elif choice == '2':
		del_task()
	
	elif choice == '3':
		print('List of to-do items:')
		print(_my_dictionary)
	elif choice == '4':
		print('Goodbye!')
	else:
		print('Please enter one of 1, 2, 3 or 4')
