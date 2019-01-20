def find(searchString, items, criteria, matchID):
    found = {}
    for id in items:
        item = items[id]
        if ((matchID and searchString.lower() in id.lower())
            or match(item, criteria, searchString)):
            found[id] = item
    
    return found

def match(item, criteria, searchString):
    for prop in criteria:
        if searchString.lower() in item[prop].lower():
            return True
    
    return False