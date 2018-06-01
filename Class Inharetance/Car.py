#Jossue Cervantes Torres, Stephen Owiti
#Homework 4 Question 1
#Car.py

class Car:

	def __init__(self, year, make):

		self.__yearModel = year
		self.__make = make
		self.__speed = 0

	#accessors

	def getSpeed(self):

		return self.__speed

	def getYear(self):

		return self.__yearModel

	def getMake(self):

		return self.__make

	#mutators

	def accelerate(self):

		self.__speed += 5

	def applyBreak(self):

		self.__speed -= 5

	def __str__(self):

		return "{0:10s} {1} {2: 4}".format(self.__make, self.__yearModel, self.__speed)