#Jossue Cervantes Torres
#Quiz 4 Question 2
#Polygon.py

#import math
import math

#class creation 
class Polygon:

	#constructor
	def __init__(self):

		#private variables
		self.__numOfSides = None
		self.__sideLength = None


	#mutators

	def sides(self, sides):

		if int(sides) > 2:

			self.__numOfSides = int(sides)
		else:
			raise ValueError("A polygon has 3 or more sides")

	def length(self, length):
		self.__sideLength = int(length)
	
	#accesors
	def getNumOfSides(self):

		return self.__numOfSides

	def getSideLength(self):

		return self.__sideLength

	def perimeter(self):

		p = self.__numOfSides*self.__sideLength
		return p

	def area(self):

		Pi = math.pi
		area = ((self.__sideLength**2)*self.__numOfSides)/(4*math.tan(Pi/self.__numOfSides))
		return area

	def __str__(self):

		return "Polygon with {0} sides of length {1} has approximate area of %.3f and perimeter of {2}"\
		.format(self.__numOfSides, self.__sideLength, self.perimeter()) %self.area()





