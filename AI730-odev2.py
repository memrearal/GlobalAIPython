# List of CV's
cvList = list()
# Create 5 dictionaries. Each dictionary should represent a CV.
cvOne = {
	"name": "John",
	"surname": "Smith",
	"job": "Assasin",
	"university": "Unknown"
}
cvTwo = {
	"name": "Jane",
	"surname": "Smith",
	"job": "Assasin",
	"university": "Unknown"
}
cvThree = {
	"name": "James",
	"surname": "Bond",
	"job": "Agent",
	"university": "Geneva"
}
cvFour = {
	"name": "Harold",
	"surname": "Finch",
	"job": "Software Engineering",
	"university": "MIT"
}
cvFive = {
	"name": "Bertram",
	"surname": "Gilfoyle",
	"job": "System Architect / Network Engineering",
	"university": "Canada"
}
# Create a CV containing the information of the 5 created people
cvList.append(cvOne)
cvList.append(cvTwo)
cvList.append(cvThree)
cvList.append(cvFour)
cvList.append(cvFive)
# Print the information on CV’s created on the screen
print("CVs:")
for cv in cvList:
	print("Name: {}, Surname: {}, Job: {}, University: {}".format(cv["name"], cv["surname"], cv["job"], cv["university"]))
