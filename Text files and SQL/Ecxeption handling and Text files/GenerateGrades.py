#Jossue Cervantes Torres, Stephen Owiti
#Homework 3 Question 4
#GenerateGrades.py

#import random module
import random


def main ():

	#dictionary for GPA with respective letter grade
	gradesDict = {4 : "A",3.67 : "A-",3.33 : "B+" , 3 : "B", 2.67 : "B-", 2.33 : "C+", 2 : "C",\
	1.67 :  "C-", 1.33 : "D+", 1 : "D" , .67 : "D-", 0 : "F"}

	
	#loop makes random number from 11 possible GPA
	gpaGrades =[4, 3.67, 3.33, 3, 2.67, 2.33, 2, 1.67, 1.33, 1, .67, 0]

	gradesList = []

	for i in range(50):
		randomGPA = random.randrange(12)
		GPA = gpaGrades[randomGPA]
		lettergrade = gradesDict[GPA]
		gradesList.append(lettergrade)

	
	#creating new text file

	gpaFile = open('grades.txt', 'w')

	count = int(len(gradesList))

	#loop uses gradesList[] to generate string lines of 10 grades each
	for i in range(0,count,10):
		line = str()

		#this loop converts list to string and appends them to string line
		for grades in gradesList[i:(i+10)]:
			line += str("%s, " %grades)
		#lines are stripped for the last comma and space at the end
		line = line.rstrip(", ")

		#lines are written to grades.txt file
		gpaFile.write("%s\n" %line)

	#file is closed
	gpaFile.close()


	#call to main function
main()