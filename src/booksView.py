import view

def printBook(id, book):
    printTitle(id, book)
    print("    Author:", book["author"])
    print("    Total copies:", book["total"])
    print("    Available: ", book["available"])
    view.printLine()

def printTitle(id, book):
    print(id + ".", book["title"], "(" + book["year"] + ")")

def getBook():

    title = view.assertInput("Title")
    author = view.assertInput("Author")
    year = view.assertNumericInput("Year")
    total = view.assertNumericInput("Total copies")

    return {
        "title": title,
        "author" : author,
        "year" : year,
        "total" : total,
        "available" : total
    }