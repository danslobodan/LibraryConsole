import menu
import loginMenu
import adminMenu
import profileMenu
import userMenu

print("Welcome to the library!")

nextMenu = menu.showMenu("login")
while nextMenu != "exit":
	nextMenu = menu.showMenu(nextMenu)

print("Goodbye!")