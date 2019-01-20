import view

def getIdInput(items):

    id = view.assertNumericInput("ID")
    if id in items:
        print("ID", id, "already exists.")
    elif id == "0":
        print("ID 0 is not allowed.")
    else:
        return id

    return 0

def getId(items):

    id = getIdInput(items)
    while id == 0:
        id = getIdInput(items)

    return id

def choseItem(items):

    if len(items) == 0:
        return 0

    if len(items) == 1:
        for id in items:
            return id

    id = input("Enter choice: ")
    if not id:
        print("Canceled.")
    elif not id.isnumeric():
        print(id, "is not a number.")
    elif id not in items:
        print("ID", id, "is not on the list.")
    else:
        return id
    
    return 0

def printItems(items, showFun):
    for key in items:
        showFun(key, items[key])