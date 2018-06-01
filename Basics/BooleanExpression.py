#GROUP 12 Jossue Cervantes, Stephen Owiti, Tyleur Reynolds
#Definition of function
def main():


	a = 6 	#variables from Question 1
	b = 9
	c = (a + b) / 2

	inventory = ["paper", "staples", "pencils"] #list

	first = "John"
	middle = "Fitzgerald"
	last = "kennedy"

	fullname = first + middle + last

#Printing Questions a - e
	print("a.", len(inventory) > 5 * len(str(fullname))) 
		#boolean expression Question 1 a

	print("b.", c  > 15)
		#boolean expression Question 1 b

	print("c.", int(a) < 8.75 < int(b))
		#boolean expression Question 1 c

	print("d.", len(str(middle)) > len(str(first)) and len(str(middle)) < len(str(last)))
		#boolean expression Question 1 d

	print("e.", len(inventory) == 0 or len(inventory) > 10)
		#boolean expression Question 1 e


#Call main function
main()