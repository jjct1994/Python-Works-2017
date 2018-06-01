#Jossue Cervantes Torres, Stephen Owiti
#Homework 3 Question 4
#GradesDistribution.py


#distribution function finds number of occurances in a list
def distribution(gradesList, x):

	listCount = []
	#for loop with if statement everytime 
	for grade in gradesList:
		#every time an especific grade accurs an x is appended to the list
		if grade == x:
			listCount += "x"
		else:
			continue
			#count of the list gives the count of accurances
	count = len(listCount)
	return count

#main function
def main():

	#file grades.txt opened for reading
	gradesFile = open("grades.txt", "r")

	#variable to translate commans into spaces
	makeBlanks = str.maketrans(",", " ")

	#list of string lines
	linesList = gradesFile.readlines()

	gradeList = []

	letterGrades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
	#loop goods line by line strips splits and removes commans 
	for lines in linesList:
		lines = lines.rstrip().translate(makeBlanks).split()
		
		#loop appends every individual grade from every line to a new list
		for grades in lines:
			gradeList.append(grades)

	print("Grade   Number of Students")

	#for loop to print out grades
	for y in letterGrades:
		print(" ", y," "*(10-int(len(y))),"%s" %distribution(gradeList, y))


	gradesFile.close()


#call to main function
main()