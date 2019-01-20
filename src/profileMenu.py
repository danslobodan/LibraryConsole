import session
import menu
import users
import admins
import credentials
import view
import userView

def editPassword(user):
	password = credentials.getPassword(user["username"])
	password = view.optionalInput("Password", password)
	credentials.updatePassword(user["username"], password)

def editUser(username):
    
    id = users.getIdByUsername(username)
    user = users.getUser(id)

    menu.printLine()
    print("Editing user: ")
    userView.printUser(id, user)
    print("Press enter to skip.")

    firstname = view.optionalInput("First name", user["firstname"])
    users.updateProperty(id, "firstname", firstname)

    lastname = view.optionalInput("Last name", user["lastname"])
    users.updateProperty(id, "lastname", lastname)

    editPassword(user)


def editAdmin(username):

    id = admins.getIdByUsername(username)
    user = admins.getAdmin(id)

    menu.printLine()
    print("Editing user: ")
    userView.printUser(id, user)
    print("Press enter to skip.")

    firstname = view.optionalInput("First name", user["firstname"])
    admins.updateProperty(id, "firstname", firstname)

    lastname = view.optionalInput("Last name", user["lastname"])
    admins.updateProperty(id, "lastname", lastname)

    editPassword(user)

def EditProfile():

    if admins.isAdmin(session.currentUser):
        editAdmin(session.currentUser)
        return "admin"
    elif users.isUser(session.currentUser):
        editUser(session.currentUser)
        return "user"

    print("Error. Current user cannot be found in admins or users.")
    return "exit"   

menu.registerHandler("editProfile", EditProfile)