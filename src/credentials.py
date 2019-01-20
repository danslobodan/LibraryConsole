import repo

CREDENTIALS = "credentials"

def getCredentials():
	return repo.getRepo(CREDENTIALS)

def add(username, password):
	if not username:
		print("Username cannot be empty.")
		return False

	if exists(username):
		print("Username", username, "is already taken.")
		return False
	
	if not password:
		print("Passowrd cannot be empty.")
		return False

	repo.addOrUpdate(CREDENTIALS, username, password)
	return True

def updatePassword(username, password):
	if not password:
		print("Password cannot be empty.")
		return False

	repo.addOrUpdate(CREDENTIALS, username, password)

def getPassword(username):
	return getCredentials()[username]

def exists(username):
	return repo.exists(CREDENTIALS, username)