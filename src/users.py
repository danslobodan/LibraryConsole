import repo

USERS = "users"
requiredFields = [ "username", "password", "firstname", "lastname" ]

users = repo.load("users")

def add(user):
	if not repo.validate(user, requiredFields):
		return False
	
	username = user["username"]
	if username in users and not users[username]["deleted"]:
		print("Username", user["username"], "already exists.")
		return False

	user["deleted"] = False
	repo.addOrUpdate(USERS, users, user["username"], user)
	return True

def addUser(user):
	user["isadmin"] = False
	return add(user)

def addAdmin(user):
	user["isadmin"] = True
	return add(user)

def get(username):
	if username not in users:
		print("User", username, "does not exist.")
		return

	return users[username]

def update(user):
	if not repo.validate(user, requiredFields):
		return False

	username = user["username"]
	if username not in users:
		print("User", username, "does not exist.")
		return False
	
	if users[username]["deleted"]:
		print("User", username, "is deleted.")
		return False

	repo.addOrUpdate(USERS, users, username, user)
	return True

def remove(username):

	if username not in users:
		print("User", username, "does not exist.")
		return False
		
	if users[username]["deleted"]:
		print("User", username, "is already deleted.")
		return False

	repo.updateProperty(USERS, users, username, "deleted", True)
	return True