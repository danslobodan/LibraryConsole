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

	return user[prop]

def updateProperty(id, prop, value):
	repo.updateProperty(USERS, id, prop, value)

def exists(id):
	return repo.exists(USERS, id)

def remove(id):
	if hasBooks(id):
		print("Error. Cannot delete a user that has lended books.")
		return False

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

def hasBooks(id):
	books = getBooks(id)
	return len(books) > 0

def getBooks(id):
	return getProperty(id, "books")

def addBook(userID, bookID):
	books = getBooks(userID)
	if bookID in books:
		print("Error. User", userID, "already has book", bookID)
		return False

	books.append(bookID)
	return True

def removeBook(userID, bookID):
	books = getBooks(userID)
	if bookID not in books:
		print("Error. User", userID, "doesn't have book", bookID)
		return False
	
	books.remove(bookID)
	return True