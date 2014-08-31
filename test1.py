from porc import Client

client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

# make sure our API key works
client.ping().raise_for_status()	

zipcode = client.get('income', 97229)

print(zipcode['median'])