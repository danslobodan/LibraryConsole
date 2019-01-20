import repo
import menu
import search

USERS = "users"

def getUsers():
	return repo.getRepo(USERS)

def getActiveUsers():
	users = getUsers()
	activeUsers = {}
	for id in users:
		if not isDeleted(id):
			activeUsers[id] = users[id]
	return activeUsers

def getUser(id):
	return repo.getItem(USERS, id)

def getIdByUsername(username):
	users = getUsers()
	for id in users:
		if users[id]["username"] == username:
			return id

def isUser(username):
	for user in getUsers().values():
		if user["username"] == username:
			return True
	return False

def addUser(id, user):

	if id not in getUsers():
		repo.addOrUpdate(USERS, id, user)
		return True

	if isDeleted(id):
		updateProperty(id, "deleted", False)
		return True
	
	print("Error. User ID", id, "already exists.")
	return False

def getProperty(id, prop):
	user = getUser(id)
	if prop not in user:
		print("Error. User", id, "doesn't have property", prop)
		return None

	return user[prop]

def updateProperty(id, prop, value):
	repo.updateProperty(USERS, id, prop, value)

def exists(id):
	return repo.exists(USERS, id)

def remove(id):

	if isDeleted(id):
		print("Error. User", id, "is already deleted.")
		return False

	repo.updateProperty(USERS, id, "deleted", True)
	return True

def isDeleted(id):
	return getProperty(id , "deleted")

def isDeletedUsername(username):
	id = getIdByUsername(username)
	return isDeleted(id)