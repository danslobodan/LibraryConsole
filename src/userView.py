import view

def printUser(id, user):
	print(id, user["firstname"], user["lastname"])

def printUsers(users):
	for id, user in users:
		printUser(id, user)

def choseUser(users):

	id = input("Enter user id: ")
	if id not in users:
		print("Invalid user id.")
		return 0
	
	if not id:
		print("User not chosen. Aborting action.")
		return 0

	return id

def getIdInput():
    id = view.assertInput("ID")
    if not id.isnumeric():
        print("ID must be a valid number")
        return 0

    return id

def getUserId(users):

    id = getIdInput()
    while id in users:
        id = getIdInput()

    return id

def getUser():

    firstname = view.assertInput("First name")
    lastname = view.assertInput("Last name")

    return {
        "firstname" : firstname,
        "lastname" : lastname
    }