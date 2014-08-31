from porc import Client

def return_scholarships(race, GPA, SAT, gender, income, other):

	client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

	searchString = ''

	if(race):
		searchString += ('race: "' + str(race) + '" OR')
	if(GPA):
		searchString += ('GPA: ["0.00" TO "' + str(GPA) + '"] OR')
	if(SAT):
		searchString += ('SAT: ["0" TO "' + str(SAT) + '"] OR')
	if(gender):
		searchString += ('gender: "' + str(gender) + '" OR')
	if(income):
		if(isinstance(income, str)):
			income = income.replace(',', '')
			income = income.replace("$", "")
		searchString += ('income: ["' + str(income) + '" TO "100000"] OR')

	if(other):
		for item in other:
			searchString += ('other-classifier: "' + str(item) + '" OR')

	if(searchString):
		searchString = searchString[:-2]

	# list all items that match our search query
	pages = client.search('scholarship', searchString)

	scholarships = []

	for page in pages:
		results = page["results"]
		for scholarship in results:
			display = scholarship["value"]
			scholarships.append({
				"title":display["title"],
				"description":display["description"],
				"link":display["link"],
				"amount":display["amount"]
				})
	return scholarships