#Jossue Cervantes Torres
#Quiz 3 Question 3
#CharacterCount.py



#counting function
def countCharacter(n, x):
	lis = []
	for i in n:  #for loop to identify the characters in the string
		if (i == x):
			lis.append(i)  #characters added to a list 

	return len(lis)   # len of list give actual count of letters


def main():

	print("\tCharacter Count Program") #title
	print()
	s = input("Enter Text:")  #input string
	print()
	char = input("Choose Character:")  #character input
	print()

	#if else statements to print the write sentence for the count

	if countCharacter(s, char) == 1:
		print("\t",char, "appears 1 time in your text.")
	elif countCharacter(s, char) == 0:
		print("\t",char, "does not appear in your text.")
	else:
		print("\t",char, "appears", countCharacter(s, char), "times in your text.")


main()