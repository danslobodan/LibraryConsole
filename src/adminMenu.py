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

	user["username"] = cred["username"]
	user["deleted"] = False
	credentials.add(cred["username"], cred["password"])
	users.addUser(id, user)
	print("Added user:", cred["username"])

	return ADMIN_MENU

def AddAdmin():

	menu.printLine()
	print("Enter admin details: ")

	cred = credentialView.getCredentials(credentials.getCredentials())
	id = userView.getUserId(admins.getAdmins())
	user = userView.getUser()

	user["username"] = cred["username"]
	credentials.add(cred["username"], cred["password"])
	admins.addAdmin(id, user)
	print("Added user:", cred["username"])

	return ADMIN_MENU

def RemoveUser():

	menu.printLine()
	print("Chose user to remove: ")
	activeUsers = users.getActiveUsers()
	userView.printUsers(activeUsers)
	id = userView.choseUser(activeUsers)
	if id == 0:
		return ADMIN_MENU

	users.remove(id)

	return ADMIN_MENU


menu.registerHandler("addUser", AddUser)
menu.registerHandler("addAdmin", AddAdmin)
menu.registerHandler("removeUser", RemoveUser)