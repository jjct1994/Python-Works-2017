#GROUP 12 Jossue Cervantes, Stephen Owiti, Tyleur Reynolds
#QUESTION 4 Homework 1

#main function
def main():

	print("	Employee Payment Calculator")
	print()
	hours = int(input("Enter the number of hours worked:"))
	print()
	hourlyPay = float(input("Enter hourly wage:"))

	print()
	print("	Employee Pay is $%.2f " %(pay(hours,hourlyPay)))



#subfunction to choose right equation
def pay(x,y):
#x = hours and y = hourly pay
	if (x <= 40):
		return(float(x * y))
	else:
		return(float((x - 40) * (1.5 * y) + 40 * y))
main()