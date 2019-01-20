import view
import tests
import books

tests.clear()

print("Testing books repository")
view.printLine()

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

view.printLine()
print("Exists")
tests.addResult(books.exists(id))
tests.addResult(not books.exists("notBook"))

view.printLine()
print("Get books")
bks = books.getBooks()
tests.addResult(len(bks) > 0)
tests.addResult(id in bks)

view.printLine()
print("Get book")
actualBook = books.getBook(id)
print(book["title"] == actualBook["title"])

view.printLine()
print("Total")
tests.addResult(books.total(id) == 1)

view.printLine()
print("Available")
tests.addResult(books.available(id) == 1)

view.printLine()
print("Lend")
tests.addResult(books.lend(id))
tests.addResult(books.available(id) == 0)
tests.addResult(not books.lend(id))

view.printLine()
print("Return")
tests.addResult(books.returnBook(id))
tests.addResult(not books.returnBook(id))

view.printLine()
print("Scrap")
tests.addResult(not books.scrap(id, 5))
tests.addResult(books.scrap(id, 1))
tests.addResult(not books.scrap(id, 1))

tests.printResult()