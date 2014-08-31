from porc import Client
import csv

client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

# make sure our API key works
client.ping().raise_for_status()

school_list = []

with open('full-need-schools.csv', 'rt') as csvfile:
	schoolreader = csv.reader(csvfile, delimiter = ',')
	for row in schoolreader:
		school_list = row


for school in school_list:
	response = client.put('schools', school, {
	  "title": school,
	  "amount":"full",
	  "income":"$24,000",
	  "other-classifier":["SNAP","reduced-lunch","FPL"]
	})
	# make sure the request succeeded
	response.raise_for_status()
# # prints the item's key
# print response.key
# # prints the item version's ref
# print response.ref