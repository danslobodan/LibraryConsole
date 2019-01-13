import json

dataFolder = "data/"

def path(repo):
	return dataFolder + repo + ".json"

def load(repo):
	with open(path(repo), "r") as file:
		return json.load(file)

def save(repo, data):
	with open(path(repo), "w") as file:
		json.dump(data, file)

def addOrUpdate(repo, data, key, value):
	data[key] = value
	save(repo, data)

def updateProperty(repo, data, key, prop, value):
	data[key][prop] = value
	save(repo, data)

def remove(repo, data, key):
	del data[key]
	save(repo, data)

def checkField(field, item):
	if field not in item:
		print("Field", field, "is required.")
		return False

	if not item[field]:
		print("Field", field, "cannot be empty.")
		return False
		
	if item[field].isspace():
		print("Field", field, "must contain characters other than whitespace.")
		return False

	return True

def validate(item, requiredFields):
	isValid = True
	for field in requiredFields:
		if not checkField(field, item):
			isValid = False
	return isValid