import repo
import datetime

LENDING = "lending"

def getDate():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def getLending():
    return repo.getRepo(LENDING)

def getUserLending(id):
    if id not in getLending():
        return {}
    
    return repo.getItem(LENDING, id)

def getBooks(userID):
    books = []
    for id in getUserLending(userID):
        books.append(id)
    return books

def hasBooks(userID):
	books = getUserLending(userID)
	return len(books) > 0

def lendBook(userID, bookID):
    books = getUserLending(userID)
    if bookID in books:
        return False

    books[bookID] = getDate()
    repo.addOrUpdate(LENDING, userID, books)
    return True

def returnBook(userID, bookID):
    books = getUserLending(userID)
    if bookID not in books:
        print("Error. User", userID, "doesn't have book", bookID)
        return False

    del books[bookID]
    repo.addOrUpdate(LENDING, userID, books)
    return True