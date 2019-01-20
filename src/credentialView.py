import view

def getUsername(credentials):

    username = view.assertInput("Username")
    if username in credentials:
        print("Username", username, "is already taken.")
        return ""

    return username

def getCredentials(credentials):

    username = getUsername(credentials)
    while username == "":
        username = getUsername(credentials)
    
    password = view.assertInput("Password")
    return {
        "username" : username,
        "password" : password
    }
