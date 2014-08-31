from porc import Client

def SNAP_est_income(household_size):
	if(household_size == None):
		return 30624
	if(household_size == 1):
		return 14940
	if(household_size == 2):
		return 20172
	if(household_size == 3):
		return 25392
	if(household_size == 4):
		return 30624
	if(household_size == 5):
		return 35844
	if(household_size == 6):
		return 41076
	if(household_size == 7):
		return 46296
	if(household_size == 8):
		return 51528
	else:
		return 51528 + 5232*(household_size - 8)

def OR_reduced_lunch_est_income(household_size):
	if(household_size == None):
		return 43568
	if(household_size == 1):
		return 21257
	if(household_size == 2):
		return 28694
	if(household_size == 3):
		return 36131
	if(household_size == 4):
		return 43568
	if(household_size == 5):
		return 51005
	if(household_size == 6):
		return 58442
	if(household_size == 7):
		return 65879
	if(household_size == 8):
		return 73316
	else:
		return 73316 + 7437*(household_size - 8)		

def reduced_lunch_est_income(household_size):
	if(household_size == None):
		return 44123
	if(household_size == 1):
		return 21590
	if(household_size == 2):
		return 29101
	if(household_size == 3):
		return 36512
	if(household_size == 4):
		return 44123
	if(household_size == 5):
		return 51634
	if(household_size == 6):
		return 59145
	if(household_size == 7):
		return 66656
	if(household_size == 8):
		return 74167
	else:
		return 74167 + 7511*(household_size - 8)		

def FPL_est_income(household_size):
	if(household_size == None):
		return 23850
	if(household_size == 1):
		return 11670
	if(household_size == 2):
		return 15730
	if(household_size == 3):
		return 19790
	if(household_size == 4):
		return 23850
	if(household_size == 5):
		return 27910
	if(household_size == 6):
		return 31970
	if(household_size == 7):
		return 36030
	if(household_size == 8):
		return 46090
	else:
		return 46090 + 4060*(household_size - 8)	

def zip_est_income(household_size, zip):
	client = Client('e6e56d2e-b91e-4dc2-aac7-ec6028c378e2')

	# make sure our API key works
	client.ping().raise_for_status()	

	zipcode = client.get('income', zip)

	return zipcode['median']