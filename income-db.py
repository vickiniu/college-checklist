from porc import Client
import csv

client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

# make sure our API key works
client.ping().raise_for_status()

income = []

with open('income.csv', 'rt') as csvfile:
	incomereader = csv.reader(csvfile, delimiter = ',')
	for row in incomereader:
		income.append({
			"ZIP":row[0],
			"median":row[1],
			"mean":row[2],
			})
		
for zipcode in income:
	response = client.put('income', zipcode["ZIP"], {
	  "ZIP": zipcode["ZIP"],
	  "median": zipcode["median"],
	  "mean": zipcode["mean"]
	})
	# make sure the request succeeded
	response.raise_for_status()