import menu
import view
import loginMenu
import adminMenu
import profileMenu
import userMenu

view.printTitle("Welcome to the library!")

nextMenu = menu.showMenu("login")
while nextMenu != "exit":
	try:
		nextMenu = menu.showMenu(nextMenu)		
	except Exception as ex:
		print(ex)
		nextMenu = menu.showMenu("login")

print("Goodbye!")