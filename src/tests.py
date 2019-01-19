results = []

def clear():
	results.clear()

def addResult(result):
	print(result)
	results.append(result)

def succeeded():
	count = 0
	for result in results:
		if result:
			count = count + 1
	return count

def failed():
	count = 0
	for result in results:
		if not result:
			count = count + 1
	return count

def printResult():
	print("-" * 50)
	print("Test results")
	print("Suceeded:", succeeded())
	print("Failed:", failed())
	print("-" * 50)