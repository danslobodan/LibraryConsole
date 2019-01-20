import search
import view
import listView

def find(itemType, items, criteria, matchID):

    searchString = input("Search " + itemType + ": ")
    if not searchString or searchString.isspace():
        print("Search canceled.")
        return {}

    found = search.find(searchString, items, criteria, matchID)
    if len(found) == 0:
        print("Zero hits.")

    return found