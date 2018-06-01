#GROUP 12 Jossue Cervantes, Stephen Owiti, Tyleur Reynolds
#definition of main fuction
#QUESTION 3 HOMEWORK 1
def main():

	#intro and instructions
	print("Welcome to Tmeperature Conversion Program")
	print()
	print("	1) Convert from Fahrenheit to Celsius.")
	print("	2) Convert from Celsius to Fahrenheit.")
	print()

	conType = float(input("Enter your choice:")) #option input
	print()
	temp = float(input("Enter temperature:")) #temperature input
	print()

	#if else to choose the right formula
	if (int(conType) == 1):
		print("	You selected Option 1")
		print()
		return(ftoCe(temp))
	elif(int(conType) == 2):
		print("	You selected Option 2")
		print()
		return(ctoFe(temp))


#Conversion formula Fahrenheit to Celsius
def ftoCe(x):
	celsius = float((5.0 / 9.0) * (x - 32))
	print(x," degrees Fahrenheit is equal to %.2f" %(celsius),"degrees Celsius.")

#Conversion formula Celsisu to Fahrenheit
def ctoFe(y):
	fahrenheit = float((9.0 / 5.0) * y + 32)
	print(y," degrees Celsius is equal to %.2f" %(fahrenheit),"degreees Fahrenheit.")


main() #call to main function