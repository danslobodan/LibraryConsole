import repo
import menu
import credentials

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
	return getUsers()[id]

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

def addOrUpdate(id, user):
	repo.addOrUpdate(USERS, id, user)

def updateProperty(id, prop, value):
	repo.updateProperty(USERS, id, prop, value)

def exists(id):
	return repo.exists(USERS, id)

def remove(id):
	repo.updateProperty(USERS, id, "deleted", True)

def addUser(id, user):
	addOrUpdate(id, user)

def isDeleted(id):
	return getUser(id)["deleted"]

def isDeletedUsername(username):
	id = getIdByUsername(username)
	return isDeleted(id)