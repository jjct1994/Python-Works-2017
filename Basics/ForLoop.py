#GROUP 12 Jossue Cervantes, Stephen Owiti, Tyleur Reynolds
#Question 2 Homework 1
def main(): #definition of main function

#QUESTION 2 A

	numList = [2,3,4,5,6,7,8,16,17,18]
		#List used for loop
	
	#Determaning if item from numList passes test	
	for i in numList:
		if(itemTest(i) == True): #call itemTest() fuction
			print(i, end=",")
	#for loop used 	
	print()
	print()

#QUESTION 2 B	

	#sequence a.
	for i in range(0,2):
		print(i, end=" ")

	print()
	print()

	#sequence b.
	for i in range(3,7):
		print(i, end=" ")

	print()
	print()

	#sequence c.
	for i in range(1,2):
		print(i, end=" ")

	print()
	print()

	#sequence d.
	for i in range(0,4,3):
		print(i, end=" ")

	print()
	print()

	#sequence e.
	for i in range(5,22,4):
		print(i, end=" ")



def itemTest(x):
	a = int(x)**2 / 8 
	return(a - int(a) == 0)
	#function to determine if the number squared is devisible by 8

	
	
#call main function
main()