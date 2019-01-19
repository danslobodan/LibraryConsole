import view
import menu
import users
import admins
import session
import credentials
import credentialView
import userView

ADMIN_MENU = "admin"

def AddUser():

	menu.printLine()
	print("Enter user details: ")

	cred = credentialView.getCredentials(credentials.getCredentials())
	id = userView.getUserId(users.getUsers())
	user = userView.getUser()

	credentials.addOrUpdate(cred["username"], cred["password"])
	users.addUser(id, user)
	print("Added user:", cred["username"])

	return ADMIN_MENU

def RemoveUser():

	menu.printLine()
	print("Chose user to remove: ")
	userView.printUsers(users.getUsers())
	id = userView.choseUser(users.getUsers())
	if id == 0:
		print("User id", id, "is invalid.")
		return ADMIN_MENU

	if not users.exists(id):
		print("User", id, "does not exist.")
		return ADMIN_MENU
		
	if users.isDeleted(id):
		print("User", id, "is already deleted.")
		return ADMIN_MENU

	user = users.getUser(id)
	credentials.remove(user["username"])
	users.remove(id)

	return ADMIN_MENU


menu.registerHandler("addUser", AddUser)
menu.registerHandler("removeUser", RemoveUser)