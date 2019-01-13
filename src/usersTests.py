import users
import tests


tests.clear()

user = { 
	"username" : "irena" , 
	"password" : "",
	"firstname" : "Irena" , 
	"lastname" : "Posza"
}

print("Users tests")
print("-" * 50)

print ("Test add password missing")
tests.addResult(not users.addAdmin(user))
print("-" * 50)

user["password"] = "irena"

print("Test add admin")
users.remove(user["username"])
tests.addResult(users.addAdmin(user))
user = users.get(user["username"])
tests.addResult(user["isadmin"])
users.remove(user["username"])
print("-" * 50)

print("Test add user")
tests.addResult(users.addUser(user))
user = users.get(user["username"])
tests.addResult(not user["isadmin"])
users.remove(user["username"])
print("-" * 50)

print("Test add existing")
users.addAdmin(user)
tests.addResult(not users.addAdmin(user))
users.remove(user["username"])
print("-" * 50)

print("Test remove non-existing")
tests.addResult(not users.remove("zika"))
print("-" * 50)

print("Test remove deleted")
tests.addResult(not users.remove(user["username"]))
print("-" * 50)

print("Test remove existing")
users.addUser(user)
tests.addResult(users.remove(user["username"]))
user = users.get(user["username"])
if user is not None:
	print(True)
else:
	print(False)
print(user["deleted"])
print("-" * 50)

print("Test update non-existing")
tests.addResult(not users.update(user))
print("-" * 50)

print("Test update deleted")
users.remove(user["username"])
tests.addResult(not users.update(user))
print("-" * 50)

print("Test update lastname")
user["lastname"] = "Posza"
users.addUser(user)
user["lastname"] = "Dan"
tests.addResult(users.update(user))
updated = users.get(user["username"])
print(user["lastname"] == updated["lastname"])
print("-" * 50)

tests.printResult()