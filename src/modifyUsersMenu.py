import menu
import users
import credentials

MODIFY_USER_MENU = "modifyUser"

def printUser(id):
	user = users.getUser(id)
	print(id, user["firstname"], user["lastname"])

def printUsers():
	for id in users.getUsers():
		printUser(id)

def choseUser():

	id = input("Enter user id: ")
	if id not in users.getUsers():
		print("Invalid user id.")
		return 0
	
	if not id:
		print("User not chosen. Aborting action.")
		return 0

	return id

def EditUser():
	
	menu.printLine()
	print("Chose user to edit: ")
	printUsers()
	id = choseUser()
	if id == 0:
		return MODIFY_USER_MENU

	print("Editing user: ")
	printUser(id)
	print("Press enter to skip.")

	fistname = input("First name: ")
	if fistname:
		users.updateProperty(id, "firstname", fistname)

	lastname = input("Last name: ")
	if lastname:
		users.updateProperty(id, "lastname", lastname)

	password = input("Password: ")
	if password:
		user = users.getUser(id)
		credentials.addOrUpdate(user["username"], password)

	if fistname or lastname or password:
		print("Updated user: ")
		printUser(id)
	else:
		print("No data was updated.")


	return MODIFY_USER_MENU

def AddUser():

	menu.printLine()
	print("Enter user details: ")
	username = menu.validateInput("Username")
	if not username:
		return MODIFY_USER_MENU

	if credentials.exists(username):
		print("Username", username, "is already taken.")
		return MODIFY_USER_MENU

	id = menu.validateInput("ID")
	if not id.isnumeric():
		print("ID must be a valid number")
		return MODIFY_USER_MENU

	if users.exists(id):
		print("ID", id, "already exists.")
		return MODIFY_USER_MENU

	password = menu.validateInput("Password")
	if not password:
		return MODIFY_USER_MENU

	firstname = menu.validateInput("First name")
	if not firstname:
		return MODIFY_USER_MENU

	lastname = menu.validateInput("Last name")
	if not lastname:
		return MODIFY_USER_MENU

	credentials.addOrUpdate(username, password)

	user = {
		"username" : username,
		"firstname" : firstname,
		"lastname" : lastname,
		"deleted" : False
	}

	users.addUser(id, user)
	print("Added user:", username)

	return MODIFY_USER_MENU

def RemoveUser():

	menu.printLine()
	print("Chose user to remove: ")
	printUsers()
	id = choseUser()
	if id == 0:
		print("User id", id, "is invalid.")
		return MODIFY_USER_MENU

	if not users.exists(id):
		print("User", id, "does not exist.")
		return MODIFY_USER_MENU
		
	if users.isDeleted(id):
		print("User", id, "is already deleted.")
		return MODIFY_USER_MENU

	user = users.getUser(id)
	credentials.remove(user["username"])
	users.remove(id)

	return MODIFY_USER_MENU


menu.registerHandler("addUser", AddUser)
menu.registerHandler("editUser", EditUser)
menu.registerHandler("removeUser", RemoveUser)