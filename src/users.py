import repo
import menu
import credentials

USERS = "users"

def getUsers():
	return repo.getRepo(USERS)

def getUser(id):
	return getUsers()[id]

def getUserByUsername(username):
	for user in getUsers().values():
		if user["username"] == username:
			return user

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
	return repo.exists(USERS, id)


def addUser(id, user):
	addOrUpdate(id, user)

def isDeleted(id):
	return getUser(id)["deleted"]





