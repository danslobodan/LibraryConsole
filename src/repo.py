import json

dataFolder = "data/"
repos = {}

def path(repo):
	return dataFolder + repo + ".json"

def getRepo(name):
	if name not in repos:
		with open(path(name), "r") as file:
			repo = json.load(file)
			repos[name] = repo
	return repos[name]

def save(name):
	with open(path(name), "w") as file:
		json.dump(repos[name], file)

def addOrUpdate(name, key, value):
	repo = getRepo(name)
	repo[key] = value
	save(name)

def updateProperty(name, key, prop, value):
	repo = getRepo(name)
	if key in repo and prop in repo[name]:
		repo[key][prop] = value
	save(name)

def exists(name, key):
	repo = getRepo(name)
	return key in repo

def remove(name, key):
	repo = getRepo(name)
	if key in repo:
		del repo[key]
		save(name)
		return True
	return False

def validate(field, value):
	if not value:
		print("Field", field, "is required.")
		return False
		
	if value.isspace():
		print("Field", field, "must contain characters other than whitespace.")
		return False

	return True