#Jossue Cervantes Torres
#Homework 2 Question 3
#IndexOfSecondLargestElement.py

import random

#main function
def main():

	#empty list to append random numbers to
	listRandom = [] #original list
	sortList = [] #list to sort and find second largest number

	#for loop to generate 10 random numbers between 1 and 20 
	for i in range(10):
		randomNumber = random.randrange(1,21)
		listRandom.append(randomNumber)   
		sortList.append(randomNumber)

		#print list of random integers
	print("List of integers:", listRandom)
	sortList.sort()

	#variable to identify largest intiger
	largestValue = int(sortList[-1])


	#if the largest number appears more than once then second to last elemnt in the sorted list will not give the second largest number
	while True:   #Loop deletes the largest number however many times in appears 
		if largestValue in sortList:     
			del sortList[sortList.index(largestValue)]
		else:
			break


	print()
	print("Second to largest number:", sortList[-1]) #after largest number is removed, sortList largest number is the last
	print()
	print("Index (position) of the second largest number:", listRandom.index(sortList[-1])) #index of second to largest number form original list






main()