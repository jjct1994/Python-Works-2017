#Jossue Cervantes Torres
#Homework 2 Question 1
#FutureValueTable.py


initialAmount = 1000

principal = initialAmount



def simInterest(n, r): #simple interst formula n= years r = rate

	simFv = principal * (1 + (r * n))
	return(simFv)

def comInterest(n, r): #compound interst formula n= years r= rate
	
	comFv = principal * (1 + r)**n
	return(comFv)



#main function
def main():

 		#values assigned for function
	year = 1

	rate = 0
	
	


	print("\tFUTURE VALUE WITH SIMPLE ANNUAL INTEREST") #title of the table
	print()
	print("Year     (5%)       (6%)       (7%)       (8%)       (9%)      (10%)")
	print("_"*70) #line to show table; number of characters counted from beginning of line year too last value at 10%, the strings printed
	for year in range(1,11):		#double forloop used because there is more than one variable (interest rate and time in years)
		for rate in range(5,11):     
			if (rate == 5):    #if statement so year corresponding to values is only printed once at the beginning of the line 
				print("%3d" %year,"  ", "$%.02f" %simInterest(year, float(rate/100)), end="   ")
			else:	
				print("$%.02f" %simInterest(year, float(rate/100)), end="   ")
		print()
	print()

		#reassigned values for compound interest different forloop
	year = 1

	rate = 0

	#Same format for the compound interest exept for the function
	print("\tFUTURE VALUE WITH COMPOUND ANNUAL INTEREST")
	print()
	
	print("Year     (5%)       (6%)       (7%)       (8%)       (9%)      (10%)")
	print("_"*70)
	for year in range(1,11):   
		for rate in range(5,11):
			if (rate == 5):  						#function used calculates compound interest insted of simple interest
				print("%3d" %year,"  ", "$%.02f" %comInterest(year, float(rate/100)), end="   ")
			else:	
				print("$%.02f" %comInterest(year, float(rate/100)), end="   ")
		print()







#call to mian function
main()