#Jossue Cervantes Torres
#Homework 2 Question 4
#(anagram)Anagrams.py

#function to see if words are anagrams or not

def isAngram(w1, w2):
	word1 = []   #empty list for each or the two words
	word2 = []

	word1 += w1  #word's characters are added and assigned to the list indipendently 
	word2 += w2
	word1.sort()  #the list of letters are sorted 
	word2.sort()

	if word1 == word2: #sorted list of letter of each word is compared in an if statetent 
		print("The words '",w1, "' and '",w2, "' are anagrams.") #print if all same letters appear in each list
	else:
		print("The words '",w1, "' and '",w2, "' are not anagrams.") #print if not all same letters appear in each list


#main function
def main():

	#ask for 2 words
	input_word1 = input("Enter the first word:")
	print()
	input_word2 = input("Enter the second word:")

	#words inputed into isAgram function
	isAngram(input_word1, input_word2)





#call to main
main()