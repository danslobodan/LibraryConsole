import view
import listView

def printUser(id, user):
	print(id, ".", user["firstname"], user["lastname"])

def getUser():

    firstname = view.assertInput("First name")
    lastname = view.assertInput("Last name")

    return {
        "firstname" : firstname,
        "lastname" : lastname
    }