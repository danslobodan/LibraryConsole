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

def addOrUpdate(repo, key, value):
	data = load(repo)
	data[key] = value
	save(repo, data)

def get(repo, key):
	data = load(repo)
	return data[key]

def updateProperty(repo, key, prop, value):
	data = load(repo)
	data[key][prop] = value
	save(repo, data)

def remove(repo, key):
	data = load(repo)
	data.remove(key)
	save(repo, data)