import menu
import books
import users
import session

import view
import listView
import booksView
import searchView

USER_MENU = "user"

def SearchBooks():

    searchCriteria = [ "author" , "title" ]
    found = searchView.find("books", books.getBooks(), searchCriteria, False)

    if len(found) > 0:
        view.printTitle("Search results:")
        listView.printItems(found, booksView.printBook)

    return USER_MENU

def UserBooks():

    userID = users.getIdByUsername(session.currentUser)
    if not users.hasBooks(userID):
        print("You currently do not have any books lended.")
        return USER_MENU

    userBooks = users.getBooks(userID)
    view.printTitle("Lended books:")
    for bookID in userBooks:
        book = books.getBook(bookID)
        booksView.printBook(bookID, book)        

    return USER_MENU

menu.registerHandler("userSearchBooks", SearchBooks)
menu.registerHandler("userBooks", UserBooks)