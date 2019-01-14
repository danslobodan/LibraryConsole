import menu

print("Welcome to the library!")

nextMenu = menu.show("login")
while nextMenu != "exit":
	nextMenu = menu.show(nextMenu)

print("Goodbye!")