import repo
import search

BOOKS = "books"

def getBooks():
    return repo.getRepo(BOOKS)

def getBook(id):
    return repo.getItem(BOOKS, id)

def add(id, book):
    books = getBooks()
    if id in books:
        print("Error. Book with ID", id, "already exists.")
        return False
    
    repo.addOrUpdate(BOOKS, id, book)
    return True

def updateProperty(id, prop, value):
    repo.updateProperty(BOOKS, id, prop, value)

def exists(id):
    return repo.exists(BOOKS, id)

def remove(id):
    return repo.remove(BOOKS, id)

def available(id):
    av = str(getBook(id)["available"])
    if not av.isnumeric():
        print("Error in books data. Available", av, "for book", id, "is not a number.")
        return 0

    av = int(av)
    return av

def total(id):
    tot = str(getBook(id)["total"])
    if not tot.isnumeric():
        print("Error in books data. Available", tot, "for book", id, "is not a number.")
        return 0

    tot = int(tot)
    return tot

def canLend(id):
    av = available(id)
    return av > 0

def lend(id):
    av = available(id)
    if av == 0:
        return False
    
    if av < 0:
        print("Error in books data. Available is negative for book", id, ".")
        return False

    av = av - 1
    updateProperty(id, "available", av)
    return True

def returnBook(id):
    av = available(id) + 1
    if av > total(id):
        print("Error. Returned more books than there is in the library. Book ID", id, ".")
        return False

    updateProperty(id, "available", av)
    return True

def scrap(id, count):
    av = available(id) - count
    if av < 0:
        print("Error. Cannot scap", count, "copies of book", id, ". Only", available(id), "available.")
        return False

    tot = total(id) - count

    updateProperty(id, "available", av)
    updateProperty(id, "total", tot)
    
    return True