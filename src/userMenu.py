import menu
import books
import users
import session

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

    found = books.find(searchString, searchCriteria)
    if len(found) > 0:
        view.printTitle("Search results:")
        listView.printItems(found, booksView.printBook)
    else:
        print("No books match the search criteria.", searchString)

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