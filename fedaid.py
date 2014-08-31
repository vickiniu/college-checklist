from porc import Client

def return_fedaid(income):

	client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

	searchString = ''

	if(income):
		if(isinstance(income, str)):
			income = income.replace(",", "")
			income = income.replace("$", "")
		searchString += ('income: ["' + str(income) + '" TO "80000"] OR ')

	searchString += ('amount: "$5,730"')

	# list all items that match our search query
	pages = client.search('government', searchString)

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

