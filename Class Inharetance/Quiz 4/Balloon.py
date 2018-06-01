#Jossue Cervantes Torres
#Quiz 4 Question 1
#Balloon.py

import math

class Balloon:

	#cunstructor for radius

	def __init__(self, radius=0.00):

		try:
			num = float(radius)
		except:

			ex = ValueError("Value must be numeric in INCHES")
			print(ex)

		else:

			self.__radius = radius

	#mutator

	def inflate(self, amount):

		try:
			num = float(amount)
		except:
			ex = ValueError("Value must be numeric in INCHES")
			print(ex)
			#raise ex
		else:
			self.__radius += amount

	#accessors

	def getVolume(self):

		Pi = math.pi

		volume = (4/3)*(self.__radius**3)*Pi

		return volume

	def getRadius(self):

		return self.__radius

	#str print method

	def __str__(self):

		return "Balloon with radius of {0} inches has volume of approximately %.2f cubic inches."\
		.format(self.__radius) %self.getVolume()









