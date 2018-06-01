#Jossue Cervantes Torres, Stephen Owiti
#Homework 3 Question 1
#NumberGrade.py

#funtion with dictionary that has all numbers of equivelent grades
def letter2GPA(input):

	gradesDict = {"A+" : 4, "A" : 4,"A-" : 3.67, "B+" : 3.33, "B" : 3, "B-" : 2.67, "C+" : 2.33, "C" : 2, "C-" : 1.67, "D+" : 1.33, "D" : 1, "D-" : .67, "F" : 0}

	#input would be letter grade
	Gpa = gradesDict[str(input)]
	
	#return of the GPA from the dictionary
	return Gpa







#main function print GPA from imput grade
def main():
	#title for program
	print("\tLetter grade to GPA program.")
	print("")

	#input variable 
	grade = input("Enter letter grade:")
	print()


	#number turned to float from function letter2GPA()
	number = float(letter2GPA(grade))

	#returning the answer to the input
	print("Your grade number is %.02f" %number)


#call to main
main()