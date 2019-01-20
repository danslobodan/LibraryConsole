import menu
import credentials
import users
import admins
import session

LOGIN_ERROR = "Invalid username or password."

def Login():

    session.currentUser = ""
    username = input("Username: ")
    password = input("Password: ")

    if not credentials.exists(username):
        print(LOGIN_ERROR)
        return "login"

    correctPassword = credentials.getPassword(username)
    if password != correctPassword:
        print(LOGIN_ERROR)
        return "login"

    if users.isUser(username):
        if users.isDeletedUsername(username):
            print(LOGIN_ERROR)
            return "login"
        else:
            session.currentUser = username
            return "user"

    if admins.isAdmin(username):
        session.currentUser = username
        return "admin"


    print("Error. No user with username: ", username)
    return "login"

menu.registerHandler("tryLogin", Login)