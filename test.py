from student import *

test = student(race = "black", GPA = "4.0", SAT = "1600", gender = "female", income = None, residency = "oregon", household_size = 4, other = ["SNAP", "reduced-lunch"], ZIP = "97229")

print(test.get_finaid())