#Jossue Cervantes Torres
#Quiz 4 Question 2
#PolygonDemo.py


#import class
import Polygon

#definition of main
def main():


	#short program title

	print("\tPolygon Driver Program")
	print()
	#input variables for sides and length
	(sides, length) = input("Enter the number of sides and length of each side separated by comma:").split(",")

	print()
	#instance of polygon created
	poly = Polygon.Polygon()
	
	#mutator methods used to assign the sides and length values
	poly.sides(sides)
	poly.length(length)

	print("Number of sides:", poly.getNumOfSides())
	print("Length of each side:", poly.getSideLength())
	print("Perimeter = ", poly.perimeter())
	print("Area = %.3f" %poly.area())

#string method from class print
	print()
	print()
	print(poly)

main()