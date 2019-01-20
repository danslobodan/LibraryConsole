import menu
import tests
import books

tests.clear()

print("Testing books repository")
menu.printLine()

id = "888"
book = {
    "title" : "TestBook",
    "year" : "9999",
    "total" : "1",
    "available" : "1",
    "author" : "TestAuthor"
}

print("Add")
tests.addResult(books.add(id, book))
tests.addResult(not books.add(id, book))

menu.printLine()
print("Exists")
tests.addResult(books.exists(id))
tests.addResult(not books.exists("notBook"))

menu.printLine()
print("Get books")
bks = books.getBooks()
tests.addResult(len(bks) > 0)
tests.addResult(id in bks)

menu.printLine()
print("Get book")
actualBook = books.getBook(id)
print(book["title"] == actualBook["title"])

menu.printLine()
print("Total")
tests.addResult(books.total(id) == 1)

menu.printLine()
print("Available")
tests.addResult(books.available(id) == 1)

menu.printLine()
print("Lend")
tests.addResult(books.lend(id))
tests.addResult(books.available(id) == 0)
tests.addResult(not books.lend(id))

menu.printLine()
print("Return")
tests.addResult(books.returnBook(id))
tests.addResult(not books.returnBook(id))

menu.printLine()
print("Scrap")
tests.addResult(not books.scrap(id, 5))
tests.addResult(books.scrap(id, 1))
tests.addResult(not books.scrap(id, 1))

criteria = [ "author", "title" ]

menu.printLine()
print("Match")
tests.addResult(books.match(book, criteria, "tEsT"))
tests.addResult(books.match(book, criteria, "stBo"))
tests.addResult(books.match(book, criteria, "autHor"))
tests.addResult(books.match(book, criteria, "sTau"))
tests.addResult(not books.match(book, criteria, "dum dum"))

menu.printLine()
print("Search")
found = books.search("88", criteria, True)
tests.addResult(len(found) == 1)
found = books.search("dum dum", criteria)
tests.addResult(len(found) == 0)

menu.printLine()
print("Admin search")
found = books.adminSearch("88")
tests.addResult(len(found) == 1)
found = books.adminSearch(id)
tests.addResult(len(found) == 1)
found = books.adminSearch("9999")
tests.addResult(len(found) == 1)

menu.printLine()
found = books.userSearch("1")
tests.addResult(len(found) == 0)
found = books.userSearch("StauTH")
tests.addResult(len(found) == 1)

menu.printLine()
print("Remove book")
tests.addResult(books.remove(id))
tests.addResult(not books.remove(id))

tests.printResult()