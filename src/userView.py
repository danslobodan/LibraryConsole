import view

def printUser(id, user):
	print(id, user["firstname"], user["lastname"])

def printUsers(users):
	for id in users:
		printUser(id, users[id])

def choseUser(users):

    id = str(input("Enter user id: "))
    if not id:
        print("User not chosen.")
    elif not id.isnumeric():
        print(id, "is not a number.")
    elif id not in users:
        print("No user with ID", id)
    elif users[id]["deleted"]:
        print("User", id, "is already deleted.")
    else:
        return id

    return 0

def getIdInput(users):

    id = view.assertNumericInput("ID")
    if id in users:
        print("User with ID", id, "already exists.")
    elif id == "0":
        print("ID 0 is not allowed.")
    else:
        return id

    return 0

def getUserId(users):

    id = getIdInput(users)
    while id == 0:
        id = getIdInput(users)

    return id

def getUser():

    firstname = view.assertInput("First name")
    lastname = view.assertInput("Last name")

    return {
        "firstname" : firstname,
        "lastname" : lastname
    }