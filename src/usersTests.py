import users
import view
import tests


tests.clear()

view.printTitle("Testing users repository")

uid = "888"
bid = "1"
user = { 
	"username" : "tusername" ,
	"firstname" : "tfirstname" , 
	"lastname" : "tlastname",
	"deleted" : False,
	"books" : []
}

view.printTitle("Add user")
tests.addResult(users.addUser(uid, user))
tests.addResult(not users.addUser(uid, user))

view.printTitle("Add book")
tests.addResult(users.addBook(uid, bid))
tests.addResult(not users.addBook(uid, bid))

view.printTitle("Return book")
tests.addResult(users.removeBook(uid, bid))
tests.addResult(not users.removeBook(uid, bid))

view.printTitle("Has books")
users.addBook(uid, bid)
tests.addResult(users.hasBooks(uid))
users.removeBook(uid, bid)
tests.addResult(not users.hasBooks(uid))

view.printTitle("Get books")
books = users.getBooks(uid)
tests.addResult(len(books) == 0)
tests.addResult(bid not in books)
users.addBook(uid, bid)
books = users.getBooks(uid)
tests.addResult(len(books) == 1)
tests.addResult(bid in books)

view.printTitle("Remove book")
tests.addResult(users.removeBook(uid, bid))
tests.addResult(not users.removeBook(uid, bid))

view.printTitle("Remove user")
tests.addResult(users.remove(uid))
tests.addResult(not users.remove(uid))

tests.printResult()