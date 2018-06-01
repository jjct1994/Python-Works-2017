#Jossue Cervantes Torres
#Quiz 3 Question 4
#StringOperations2.py



#main function
def main():


	s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ...'''

	print(s)
	#replace character: .,:\n with spaces 
	blanks = str.maketrans(".,;\n", 4*" ")
	
	#replacement in string and new string created
	newS = s.translate(blanks)

	#leading and trailing blank spaces removed
	newS = s.translate(blanks).strip()

	#turns all letters into lowercase
	newS = newS.lower()
	print()

	#count of substring it was with in main string
	count = newS.count("it was")
	print("Count of String('it was'):", count)
	
	#Replaces all was string with is strings
	newS = newS.replace('was', "is")

	#slpiting individual words to  a new list
	listS = newS.split()
	for i in listS:
		print(i)

#call to main function
main()