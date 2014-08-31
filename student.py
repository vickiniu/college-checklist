from porc import Client
from income import *
from scholarship import *
from fedaid import *
from finaid import *

class student:
	def __init__(self, race, GPA, SAT, gender, income, residency, household_size, other, ZIP):
		self.__race = race
		if(GPA):
			self.__GPA = float(GPA)
		else:
			self.__GPA = None
		if(SAT):
			self.__SAT = float(SAT)
		else:
			self.__SAT = None
		self.__gender = gender
		if(income):
			if(isinstance(income, str)):
				self.__income = float(income[1:])
			else:
				self.__income = income
		else:
			self.__income = None
		self.__residency = residency
		if(household_size):
			self.__household_size = int(household_size)
		else:
			self.__household_size = None
		self.__other = other
		if(ZIP):
			self.__zip = int(ZIP)
		else:
			self.__zip = None
		scholarships = None
		federalaid = None
		financialaid = None

		self.estimate_income()

	#If student doesn't input income, estimates based on
	#other factors -- ZIP code, SNAP eligibility, etc
	def estimate_income(self):
		if(self.__income != None):
			return self.__income
		if(self.__other != None):
			if "SNAP" in self.__other:
				self.__income = SNAP_est_income(self.__household_size)
				return self.__income
			if "reduced-lunch" in self.__other:
				if(self.__residency == "oregon"):
					self.__income = OR_reduced_lunch_est_income(self.__household_size)
					return self.__income
				else:
					self.__income = reduced_lunch_est_income(self.__household_size)
					return self.__income
			if "FPL" in self.__other:
				self.__income = FPL_est_income(self.__household_size)
				return self.__income
		if(self.__zip != None):
			self.__income = zip_est_income(self.__household_size, self.__zip)
			return self.__income
		else:
			return None

	def return_income(self):
		return self.__income

	def get_scholarships(self):
		return return_scholarships(self.__race, self.__GPA, self.__SAT, self.__gender, self.__income, self.__other)

	def get_fedaid(self):
		return return_fedaid(self.__income)

	def get_finaid(self):
		return return_finaid(self.__income, self.__other)