import search
import view
import listView

def criteriaString(criteria, matchID):

    if matchID:
        criteria = ["ID"] + criteria

    l = len(criteria)
    if l == 0:
        return ""

    string = ""
    for i in range(0, l):
        string = string + criteria[i]
        if i < l - 2:
            string = string + ", "
        elif i < l - 1:
            string = string + " or "

    return string

def find(itemType, items, criteria, matchID):

    message = "Search " + itemType + " by " + criteriaString(criteria, matchID) + ": "
    searchString = input(message)
    if not searchString or searchString.isspace():
        print("Search canceled.")
        return {}

    found = search.find(searchString, items, criteria, matchID)
    if len(found) == 0:
        print("No", itemType, "match the search criteria.")

    return found