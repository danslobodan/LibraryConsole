import menu
import view
import loginMenu
import adminMenu
import profileMenu
import userMenu

view.printTitle("Welcome to the library!")

nextMenu = menu.showMenu("login")
while nextMenu != "exit":
	nextMenu = menu.showMenu(nextMenu)

print("Goodbye!")