#Jossue Cervantes Torres, Stephen Owiti
#Homework 4 Question 2
#Square.py


#importing Polygon
from Polygon import Polygon

#subclass Square from parent class polygon
class Square(Polygon):

	#Subclass constructor with only length as argument
	def __init__(self, length):

		#using super class constructor so not to creat new instance variables 
		super().__init__(4, length)
		super().perimeter()
		super().getNumOfSides()
		super().getSideLength()
		

	#new method calls for area from superclass
	def getArea(self):


		return super().area()


	#string method to print perimeter and area
	def __str__(self):

		return "Perimeter: {0}  Area: {1: .2f}".format(super().perimeter(), self.getArea())