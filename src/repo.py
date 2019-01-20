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

def getItem(name, key):
	repo = getRepo(name)
	return repo[key]

def save(name):
	with open(path(name), "w") as file:
		json.dump(repos[name], file)

def addOrUpdate(name, key, value):
	repo = getRepo(name)
	repo[key] = value
	save(name)

def updateProperty(name, key, prop, value):
	repo = getRepo(name)
	key = str(key)
	if key in repo and prop in repo[key]:
		repo[key][prop] = value
	
	save(name)

def exists(name, key):
	repo = getRepo(name)
	key = str(key)
	return key in repo

def remove(name, key):
	repo = getRepo(name)
	key = str(key)
	if key in repo:
		del repo[key]
		save(name)
		return True
	
	return False