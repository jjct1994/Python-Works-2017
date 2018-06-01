#Jossue Cervantes Torres
#Quiz 3 Question 1
#Unique.py

#importing random module for random functions
import random

#function to exclude repeated letters 
def excludeLetter(x, liss, liss2):

	repeat = x + 32
	#since characters lower and upper case
	if x in liss:
		liss2.append(chr(x))
	elif repeat in liss:          #adding 32 to upper case finds its respective letter in uppercase
		liss2.append(chr(x))
	else:
		liss.append(x)
#this loop will append random letter that hasnt been used to Unique list
#and any other letter to excluded list

def generateUniqueList(list1, list2):


	
	randomNum = 0
	#looop to generate 15 random numbers 
	while(len(list1) < 15):
		randomNum = random.randrange(65,123)
		if randomNum in range(91,97): #if character values not within alphabet 
			continue                  #then they are ignored and loop continues
		else:
			excludeLetter(randomNum, list1, list2) #for all others within alphabet
												   #excludeLetter functions finds out if
												   #they are repeated or not to append to right list

	#this loop converts the appended values to actual characters											   
	for num in range(0,15):
		character = chr(list1[0])
		list1.append(character)
		list1.remove(list1[0])
		
#main function of program
def displayList():

	uniqueList = []
	excludedList = []

	#function inputed for rispective lists uniqueList and excludedList
	generateUniqueList(uniqueList, excludedList)

	uniqueList.insert(0, "List with random characters:  ")
	length = len(excludedList)
	excludedList.insert(0, "List with excluded characters:")

	#short title
	print("\t15 Random Characters")
	print()

	#pirnts random character list of 15
	for i in uniqueList:
		print(i, end=" ")

	print()
	print()
	#prints excluded values
	for i in excludedList:
		print(i, end=" ")
	print()
	print()
	#counts total values in exclude list
	print("Number of excluded characters:", (len(excludedList)-1))

displayList()


