#Jossue Cervantes Torres, Stephen Owiti
#Homework 3 question 2
#MirrorImage.py

def mirror(input):

	#letters with mirror letters, 0 for the ones that dont have mirror letters
	mirrorLetters = {"a" : "0","b" : "d","c" : "0", "d" : "b", "e" : "0", "f" : "0", "g" : "0", "h" : "0",\
	 "i" : "i", "j" : "0", "k" : "0", "l" : "l", "m" : "m","n" : "0", "o" : "o", "p" : "q", "q" : "p",\
	 "r" : "0", "s" : "0","t" : "0", "u" : "u", "v" : "v", "w" : "w", "x" : "x", "y" : "0", "z" : "0"}

	mirrorWord = ""

	#for loop to add mirror letters to mirror string
	for i in input:
		mirrorWord += mirrorLetters[i]

	#function return mirror word but needs to be reversed for it to be actually mirrored
	return mirrorWord[::-1]

#main function
def main():
	print("\tMirror Image program")
	print()

#input variable to get word to analize
	inputWord = input("Enter word:")

	print()

	#if else statement if mirror word can be mirrored than it gets printed
	if "0" in mirror(inputWord): #letters that dont have mirror letter will appear as 0s in thword
		print("The word", inputWord, "cannot have a mirror image")
	else:
		print("Mirror image of", inputWord, "is", mirror(inputWord))

main()



