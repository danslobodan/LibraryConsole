import repo

menus = repo.load("menus")
handlers = {}

def registerHandler(menu, handler):
	handlers[menu] = handler

def printMenu(menu):
	print(menu["title"])
	options = menu["options"]
	for i in options:
		print(i + ".", options[i]["text"])

def takeInput(menu):
	printMenu(menu)
	num = input("Please enter a number: ")
	
	if not num.isdigit():
		print("Please enter a valid digit.")
		return 0

	if num not in menu["options"]:
		print("Invalid choice. Please try again.")
		return 0
	
	return num

def show(menuName):

	menu = menus[menuName]

	if "returnTo" in menu:
		return menu["returnTo"]

	choice = takeInput(menu)
	while choice == 0:
		choice = takeInput(menu)

	chosenMenu = menu["options"][choice]["menu"]

	if chosenMenu in handlers:
		handlers[chosenMenu]()

	return chosenMenu