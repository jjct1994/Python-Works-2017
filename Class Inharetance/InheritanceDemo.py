#Jossue Cervantes Torres, Stephen Owiti
#Homework 4 Question 2
#InheritanceDemo.py

#importing both subclass 
from Triangle import Triangle
from Square import Square

#main function
def main():

	#square and triangle objects
	S1 = Square(2)
	T1 = Triangle(3)

	#Pint objects T1 and S1
	print("Square with side length of 2\n",S1)
	print()
	print("Triangle with side length of 3\n", T1)

main()

