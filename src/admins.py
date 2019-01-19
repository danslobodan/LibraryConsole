import repo
import menu
import credentials

ADMINS = "admins"

def getAdmins():
	return repo.getRepo(ADMINS)

def getAdmin(id):
	return getAdmins()[id]

def getIdByUsername(username):
	admins = getAdmins()
	for id in admins:
		if admins[id]["username"] == username:
			return id

def isAdmin(username):
	for admin in getAdmins().values():
		if admin["username"] == username:
			return True
	return False

def addOrUpdate(id, admin):
	repo.addOrUpdate(ADMINS, id, admin)

def updateProperty(id, prop, value):
	repo.updateProperty(ADMINS, id, prop, value)

def exists(id):
	return repo.exists(ADMINS, id)

def remove(id):
	return repo.exists(ADMINS, id)

def addAdmin(id, admin):
	addOrUpdate(id, admin)

def isDeleted(id):
	return getAdmin(id)["deleted"]



