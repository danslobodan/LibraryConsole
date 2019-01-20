import view

def printBook(id, book):
    print(id + ".", book["title"], "(" + book["year"] + ")")
    print("    Author:", book["author"])
    print("    Total copies:", book["total"])
    print("    Available: ", book["available"])

