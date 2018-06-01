#Jossue Cervantes Torres
#Quiz 2 Question 2
#Depreciation.py
def depreciation(n):    #Formula for straight line depreciation
	annualValue = 586000 - (1500*12)*n
	return(annualValue)

def depreciationPer(x):		#Formula for 3% depretiation
	annualV = 586000 * .97 ** x
	return(annualV)

#main formula
def main():

	value = 0
			#call Function with formula
	while (depreciation(value) > 370000):

		value += 1


		print("Year:", value, "Depreciated value: %.2f" %depreciation(value))


	print()
	print()

	year = 0
			#call to function with formula
	while (depreciationPer(year) > 370000):

		year += 1


		print("Year:", year, "Depreciated value: %.2f" %depreciationPer(year))











main()