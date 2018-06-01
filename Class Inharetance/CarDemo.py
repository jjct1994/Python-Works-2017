#Jossue Cervantes Torres, Stephen Owiti
#Homework 4 Question 1
#CarDemo.py

import Car

def main():

	#car objects created with different cars
	
	c1 = Car.Car(2009, "Toyota")
	c2 = Car.Car(2012, "Ford")
	c3 = Car.Car(2015, "Honda")

	#String representation all 3 cars
	print("  MAKE    YEAR    SPEED")
	print(c1)
	print(c2)
	print(c3)


	print()

	#accelerate 5 times 
	print("Accelerating {0} {1}". format(c1.getYear(), c1.getMake()))
	for i in range(6):
		print("{0}".format(c1.getSpeed()), end=" ")
		if c1.getSpeed() < 22:
			c1.accelerate()

	print()
	print()
	#loop using applyBreak() 5 times
	print("Applying break to {0} {1}". format(c1.getYear(), c1.getMake()))
	for i in range(6):
		print("{0}".format(c1.getSpeed()), end=" ")
		c1.applyBreak()


main()
