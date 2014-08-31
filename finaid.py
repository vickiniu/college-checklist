from porc import Client

def return_finaid(income, other):
	eligible = False

	if(income):
		if(isinstance(income, str)):
			income = income.replace("$", "")
			income = income.replace(",", "")
			income = int(income)
		if(income < 24000):
			eligible = True

	if(other):
		if(("SNAP" in other) or ("reduced-lunch" in other) or ("FPL" in other)):
			eligible = True

	colleges = [{}]


	if(eligible):
		client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

		pages = client.list('schools')

		for page in pages:
			results = page["results"]
			for college in results:
				display = college["value"]
				colleges.append({
					"title":display["title"],
					"amount":"full"})
	return colleges