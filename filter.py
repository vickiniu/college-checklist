import sys
from student import *

def dict_format(dictionary):
	return_string = ''
	for entry in dictionary:
		if("title" in entry.keys()):
			return_string += (entry["title"].replace('\'', '') + '\n')
		if("description" in entry.keys()):
			return_string += (entry["description"] + '\n')
		if("link" in entry.keys()):
			return_string += (entry["link"] + '\n')
		if("amount" in entry.keys()):
			if(entry["amount"] == "full"):
				return_string += ("Full tuition" + '\n')
			else:
				return_string += (entry["amount"] + '\n')
		return_string += '\n'
	return return_string

race = sys.argv[1]
if(race == "0"):
	race = None
GPA = sys.argv[2]
if(GPA == "0"):
	GPA = None
SAT = sys.argv[3]
if(SAT == "0"):
	SAT = None
gender = sys.argv[4]
if(gender == "0"):
	SAT = None
income = sys.argv[5]
if(income == "0"):	income = None
residency = sys.argv[6]
if(residency == "0"):
	residency = None
household_size = sys.argv[7]
if(household_size == "0"):
	household_size = None
other = sys.argv[8]
if(other == "0"):
	other = None
ZIP = sys.argv[9]
if(ZIP == "0"):
	ZIP = None

instance = student(race = race, GPA = GPA, SAT = SAT, gender = gender, income = income, residency = residency, household_size = household_size, other = other, ZIP = ZIP)

scholarships = dict_format(instance.get_scholarships())
finaid = dict_format(instance.get_finaid())
fedaid = dict_format(instance.get_fedaid())

print(scholarships)
print(finaid)
print(fedaid)
