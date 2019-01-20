import menu
import books
import view
import listView
import booksView

USER_MENU = "user"

def SearchBooks():

    searchCriteria = [ "author" , "title" ]
    searchString = input("Enter author or title: ")
    if not searchString or searchString.isspace():
        print("Search aborted.")
        return USER_MENU

    found = books.search(searchString, searchCriteria)
    if len(found) > 0:
        listView.printItems(found, booksView.printBook)
    else:
        print("Found no books for query", searchString)

    return USER_MENU


menu.registerHandler("userSearchBooks", SearchBooks)