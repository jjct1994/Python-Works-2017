
def main():


	a = int(input("Enter temperature in degrees fahrenheit:"))


	if a > 100:
		print("Temperature of", a ,"degrees is Blazing")
	else:
		if a < 20:
			print("Temperature of", a , "degrees is Frigid.")
		elif a <= 39:
			print("Temperature of", a , "degrees is Cold.")
		elif a <= 65:
			print("Temperature of", a , "degrees is Cool.")
		elif a <= 90:
			print("Tmeperature of", a , "degrees is Warm.")
		else:
			print("Temperature of", a , "degrees is Hot.")

main()