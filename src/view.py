def assertInput(inputName):

    value = validateInput(inputName)
    while value == "":
        value = validateInput(inputName)

    return value

def validateInput(inputName):

	value = input(inputName + ": ")
	if not value:
		print(inputName, "is required.")
		return ""
		
	if value.isspace():
		print(inputName, "must contain characters other than whitespace.")
		return ""

	return value

def optionalInput(inputName, value):

	newValue = input(inputName)
	if not newValue or newValue.isspace():
		print(inputName, "was skipped.")
		return value

	return newValue