#Jossue Cervantes Torres
#Quiz 3 Question 2
#StringOperations1



#main function
def main():



	s = "Welcome to Python Programming"

	#Question 2 part a____________________________________________
	#printing booliean expressions for every problem
	sA = s[11:13]

	print("sA = s[11:13] is ", sA == 'Py')

	sB = s[7:11]

	print("sB = s[7:11] is ", sB =='gram')

	sC = s[-23:-40]

	print("sC = s[-23:-40] is ", sC == 'Welcome')

	sD = s[11:(len(s) - 12)]

	print("sD = s[11:(len(s) - 12)] is ", sD == 'Python')
	print()



	#Question 2 part b ________________________________________________

	s = 'Welcome to Python Programming' #original string
	print("Question 2 Part B:")
	print()

	#Part A
	#striping left part sting      striping right part of string
	s2 = s.lstrip('Welcome to').rstrip("Programming").rstrip()
	print()
	
	print("a.", s2)


	#Part B
	#striping the right part of the string since only the first word is to be printed
	s2 = s.rstrip("to Python Programming").rstrip()
	print("b.", s2)


	#Question 2 Part c ______________________________________________________
	print()
	print("#Question 2 Part c")
	s = 'abcdefghijklmnopqrstuvwxyz' #original string
	
	#variables defined
	length = len(s) #length of original string
	great = []
	python = []
	print(s)
	#appending letters of words to list to then look for them in string s
	great += 'great'
	python += 'python'

	print()
	#loop to find the letter in the string remove it and add it to the end of string
	for letter in great:
		s = s.replace(letter, "-")
		s += letter
		print
	print(s[(len(great)*(-1)):]) #printing slice of original list
	print()
	##loop to find the letter in the string remove it and add it to the end of string
	for letter in python:
		s = s.replace(letter, "-")
		s += letter
	print(s[(len(python)*(-1)):])#printing slice of original list to print word

	print()

	#printing string after letters were used for the words
	print(s[:length])


#call to main
main()
