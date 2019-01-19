import repo

MENUS = "menus"
handlers = {}

def getMenus():
	return repo.getRepo(MENUS)

def getMenu(name):
	return getMenus()[name]

def exists(menuName):
	return menuName in getMenus()

def registerHandler(menuName, handler):
	handlers[menuName] = handler

def printMenu(menu):
	print(menu["title"])
	options = menu["options"]
	for i in options:
		print(i + ".", options[i]["text"])

def takeInput(menu):
	num = input("Please enter a number: ")
	
	if not num.isdigit():
		print("Please enter a valid digit.")
		return 0

	if num not in menu["options"]:
		print("Invalid choice. Please try again.")
		return 0
	
	return num

def choseMenu(menu):
	printMenu(menu)
	choice = takeInput(menu)
	return choice

def showMenu(name):

	if name in handlers:
		return handlers[name]()

	if not exists(name):
		print("Menu not found. Exiting")
		return "exit"

	menu = getMenu(name)
	choice = choseMenu(menu)
	while choice == 0:
		choice = choseMenu(menu)

	chosenMenu = menu["options"][choice]["menu"]
	
	return chosenMenu