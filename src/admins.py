import repo
import menu
import credentials

ADMINS = "admins"

def getAdmins():
	return repo.getRepo(ADMINS)

def getAdmin(id):
	return getAdmins()[id]

def getAdminByUsername(username):
	for admin in getAdmins().values():
		if admin["username"] == username:
			return admin

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



